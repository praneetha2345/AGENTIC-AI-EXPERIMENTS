import ollama
import os

MODEL = "llama3.2-vision"

def main():
    image_path = input("Enter image path: ")

    if not os.path.exists(image_path):
        print("Image not found.")
        return

    question = input("Ask a question about the image: ")

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question,
                "images": [image_path]
            }
        ]
    )

    print("\nVISUAL QA RESULT")
    print("=" * 50)
    print(response["message"]["content"])

if __name__ == "__main__":
    main()