import ollama

MODEL = "llama3.2"

def ask_llm(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a policy compliance evaluation agent."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"]

def main():
    policy = """
    Company Policy:
    1. Customer personal data must not be shared publicly.
    2. Passwords must never be stored in plain text.
    3. Confidential company files must use access control.
    4. AI-generated content must be reviewed before publication.
    """

    scenario = """
    An employee uploaded a customer database containing names,
    phone numbers and email addresses to a public file-sharing website.
    The database was not encrypted and no access restriction was applied.
    """

    prompt = f"""
Evaluate the following scenario against the company policy.

POLICY:
{policy}

SCENARIO:
{scenario}

Return:
1. Compliance status
2. Violated rules
3. Severity
4. Reason
5. Recommended remediation
"""

    print("POLICY COMPLIANCE REPORT")
    print("=" * 50)
    print(ask_llm(prompt))

if __name__ == "__main__":
    main()