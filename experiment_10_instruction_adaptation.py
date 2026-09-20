import ollama

MODEL = "llama3.2"

training_examples = """
Example 1:
Input: Java is a programming language.
Output: JAVA

Example 2:
Input: Python is easy to learn.
Output: PYTHON

Example 3:
Input: SQL is used for databases.
Output: SQL
"""

def main():
    user_input = input("Enter a sentence: ")

    prompt = f"""
You are an instruction-following model.

Learn the output pattern from these examples:

{training_examples}

Now process the following input:

{user_input}

Return only the main technology or programming language
mentioned in the sentence.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\nADAPTED MODEL OUTPUT")
    print("=" * 50)
    print(response["message"]["content"])

if __name__ == "__main__":
    main()