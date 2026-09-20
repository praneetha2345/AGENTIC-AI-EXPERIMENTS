import ollama
import time

MODELS = [
    "llama3.2"
]

questions = [
    "What is artificial intelligence?",
    "Explain machine learning in simple words.",
    "What is an AI agent?"
]

def test_model(model):
    total_time = 0
    total_tokens = 0

    print(f"\nMODEL: {model}")
    print("=" * 50)

    for question in questions:
        start = time.perf_counter()

        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        elapsed = time.perf_counter() - start

        text = response["message"]["content"]
        total_time += elapsed

        print("\nQuestion:", question)
        print("Answer:", text)
        print(f"Response time: {elapsed:.2f} seconds")

        if "eval_count" in response:
            total_tokens += response["eval_count"]

    print("\nPERFORMANCE")
    print("-" * 50)
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Total output tokens: {total_tokens}")

    if total_time > 0:
        print(f"Tokens/second: {total_tokens / total_time:.2f}")

def main():
    for model in MODELS:
        test_model(model)

if __name__ == "__main__":
    main()