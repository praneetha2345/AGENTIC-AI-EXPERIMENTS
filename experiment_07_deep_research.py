import ollama

MODEL = "llama3.2"

def ask(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a research planning and synthesis agent."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"]

def main():
    topic = input("Enter research topic: ")

    plan_prompt = f"""
Create a research plan for the topic:

{topic}

Divide the topic into 4 important subtopics.
Give one research question for each subtopic.
"""

    plan = ask(plan_prompt)

    print("\nRESEARCH PLAN")
    print("=" * 50)
    print(plan)

    research_prompt = f"""
You are conducting a technical research study.

Topic:
{topic}

Research plan:
{plan}

Prepare a detailed research report containing:
1. Introduction
2. Important concepts
3. Current technologies
4. Advantages
5. Limitations
6. Applications
7. Future scope

Do not invent citations.
"""

    report = ask(research_prompt)

    print("\nFINAL RESEARCH REPORT")
    print("=" * 50)
    print(report)

if __name__ == "__main__":
    main()