from ollama import chat

MODEL = "llama3.2"

text = input("Enter text to summarize:\n")

# Step 1
prompt1 = f"""
Summarize the following text in 5 simple sentences.

Text:
{text}
"""

response1 = chat(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt1}
    ]
)

summary = response1.message.content

print("\nSTEP 1 - SUMMARY")
print(summary)

# Step 2
prompt2 = f"""
Read this summary:

{summary}

Extract the 5 most important points.
"""

response2 = chat(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt2}
    ]
)

key_points = response2.message.content

print("\nSTEP 2 - KEY POINTS")
print(key_points)

# Step 3
prompt3 = f"""
Read these key points:

{key_points}

Create 3 questions to test understanding.
"""

response3 = chat(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt3}
    ]
)

questions = response3.message.content

print("\nSTEP 3 - QUESTIONS")
print(questions)

print("\nPROMPT CHAIN COMPLETED")