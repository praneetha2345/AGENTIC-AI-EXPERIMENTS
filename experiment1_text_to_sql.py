import sqlite3
from ollama import chat

MODEL = "llama3.2"

db = sqlite3.connect("company.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

cursor.execute("SELECT COUNT(*) FROM employees")

if cursor.fetchone()[0] == 0:
    data = [
        (1, "John", "IT", 60000),
        (2, "Alice", "HR", 50000),
        (3, "Bob", "IT", 70000),
        (4, "David", "Sales", 55000),
        (5, "Emma", "Finance", 65000)
    ]

    cursor.executemany(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        data
    )

    db.commit()

schema = """
employees(
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
)
"""

question = input("Ask a question: ")

prompt = f"""
You are a Text-to-SQL assistant.

Database schema:
{schema}

User question:
{question}

Generate only a SQLite SELECT query.

Do not generate INSERT, UPDATE, DELETE or DROP.
"""

response = chat(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

sql = response.message.content.strip()

sql = sql.replace("```sql", "")
sql = sql.replace("```", "")
sql = sql.strip()

print("\nGenerated SQL:")
print(sql)

if not sql.upper().startswith("SELECT"):
    print("\nOnly SELECT queries are allowed.")
else:
    try:
        cursor.execute(sql)
        result = cursor.fetchall()

        print("\nDatabase Result:")

        for row in result:
            print(row)

        answer_prompt = f"""
User question:
{question}

SQL result:
{result}

Explain the result in simple English.
"""

        answer = chat(
            model=MODEL,
            messages=[
                {"role": "user", "content": answer_prompt}
            ]
        )

        print("\nFinal Answer:")
        print(answer.message.content)

    except Exception as e:
        print("\nSQL Error:")
        print(e)

db.close()