import sqlite3
from ollama import chat

MODEL = "llama3.2"

db = sqlite3.connect("sales.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER,
    product TEXT,
    quantity INTEGER,
    price INTEGER
)
""")

cursor.execute("SELECT COUNT(*) FROM sales")

if cursor.fetchone()[0] == 0:
    data = [
        (1, "Laptop", 5, 50000),
        (2, "Phone", 10, 20000),
        (3, "Tablet", 7, 15000),
        (4, "Monitor", 8, 12000),
        (5, "Keyboard", 20, 2000)
    ]

    cursor.executemany(
        "INSERT INTO sales VALUES (?, ?, ?, ?)",
        data
    )

    db.commit()


def run_sql(sql: str) -> str:
    """
    Execute a SELECT SQL query on the sales database.

    Args:
        sql: SQL SELECT query.

    Returns:
        Database query result.
    """

    if not sql.strip().upper().startswith("SELECT"):
        return "Only SELECT queries are allowed."

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return str(result)

    except Exception as e:
        return "SQL Error: " + str(e)


tools = [run_sql]

question = input("Ask a question about sales: ")

messages = [
    {
        "role": "system",
        "content": """
You are a SQL database agent.

Use the run_sql tool whenever the user asks
about information stored in the sales database.

Only generate SELECT queries.
Do not modify the database.
"""
    },
    {
        "role": "user",
        "content": question
    }
]

print("\nAgent is working...")

while True:

    response = chat(
        model=MODEL,
        messages=messages,
        tools=tools
    )

    messages.append(response.message)

    if response.message.tool_calls:

        for call in response.message.tool_calls:

            function_name = call.function.name
            arguments = call.function.arguments

            print("\nTool:", function_name)
            print("Arguments:", arguments)

            if function_name == "run_sql":
                result = run_sql(**arguments)
            else:
                result = "Unknown tool."

            print("Tool Result:", result)

            messages.append({
                "role": "tool",
                "tool_name": function_name,
                "content": result
            })

    else:
        print("\nFinal Answer:")
        print(response.message.content)
        break

db.close()