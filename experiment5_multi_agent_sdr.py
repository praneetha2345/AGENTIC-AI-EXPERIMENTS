from ollama import chat

MODEL = "llama3.2"


def ask_agent(role, task):

    prompt = f"""
You are a {role}.

Your task:
{task}

Give clear and useful results.
"""

    response = chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.message.content


def lead_generation(industry):

    task = f"""
Generate 5 example B2B companies that could be
potential customers in the {industry} industry.

For each company provide:

1. Company name
2. Industry
3. Company type
4. Possible business need

Use fictional/example companies.
Do not provide private personal information.
"""

    return ask_agent(
        "Lead Generation Agent",
        task
    )


def lead_qualification(leads):

    task = f"""
Analyze the following potential leads:

{leads}

For every lead provide:

1. Company
2. Score from 1 to 10
3. Reason for the score
4. Priority: HIGH, MEDIUM or LOW
"""

    return ask_agent(
        "Lead Qualification Agent",
        task
    )


def email_generation(qualified_leads):

    task = f"""
Create professional outreach email templates
for the following qualified leads:

{qualified_leads}

Rules:

- Keep the email short.
- Make it professional.
- Do not invent personal information.
- Do not claim that an email has actually been sent.
- Create emails only for HIGH priority leads.
"""

    return ask_agent(
        "Email Generation Agent",
        task
    )


def main():

    print("=" * 60)
    print("MULTI-AGENT SDR SYSTEM")
    print("=" * 60)

    industry = input("\nEnter target industry: ")

    print("\n[AGENT 1] Lead Generation Agent")
    print("--------------------------------")

    leads = lead_generation(industry)

    print(leads)

    print("\n[AGENT 2] Lead Qualification Agent")
    print("-----------------------------------")

    qualified = lead_qualification(leads)

    print(qualified)

    print("\n[AGENT 3] Email Generation Agent")
    print("--------------------------------")

    emails = email_generation(qualified)

    print(emails)

    print("\n" + "=" * 60)
    print("MULTI-AGENT WORKFLOW COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()