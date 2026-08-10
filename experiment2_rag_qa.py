from ollama import chat
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MODEL = "llama3.2"

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

documents = [
    x.strip()
    for x in text.split("\n\n")
    if x.strip()
]

print("Creating document index...")

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

print("RAG system ready.")

question = input("\nAsk a question: ")

query_vector = vectorizer.transform([question])

scores = cosine_similarity(
    query_vector,
    vectors
)[0]

top_indices = scores.argsort()[-3:][::-1]

context = ""

for index in top_indices:
    context += documents[index] + "\n\n"

print("\nRetrieved Documents:")
print(context)

prompt = f"""
You are a RAG question answering system.

Answer the question only using the context.

Context:
{context}

Question:
{question}

If the answer is not available in the context,
say "I don't have enough information."

Give a simple answer.
"""

response = chat(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nFinal Answer:")
print(response.message.content)