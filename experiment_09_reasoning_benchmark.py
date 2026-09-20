import ollama
import time

MODEL = "llama3.2"

questions = [
    "If all roses are flowers and some flowers are red, can we conclude that some roses are red? Explain.",
    "A train travels 60 km in 1 hour. How far will it travel in 3.5 hours?",
    "There are 5 boxes. Each box contains 8 books. If 7 books are removed, how many remain?",
    "What is the next number in this sequence: 2, 4, 8, 16, 32?"
]

def ask(question):
    start = time.perf_counter()

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Solve problems carefully. Give the final answer clearly."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    elapsed = time.perf_counter() - start

    return response["message"]["content"], elapsed

def main():
    print("REASONING BENCHMARK")
    print("=" * 60)

    total_time = 0

    for i, question in enumerate(questions, 1):
        answer, elapsed = ask(question)

        total_time += elapsed

        print(f"\nQuestion {i}")
        print("-" * 40)
        print(question)

        print("\nAnswer:")
        print(answer)

        print(f"\nTime: {elapsed:.2f} seconds")

    print("\n" + "=" * 60)
    print(f"Total execution time: {total_time:.2f} seconds")
    print(f"Average time: {total_time / len(questions):.2f} seconds")

if __name__ == "__main__":
    main()