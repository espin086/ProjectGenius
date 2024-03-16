from openai import OpenAI

client = OpenAI()


def text_generation(prompt: str, model: str = "gpt-4") -> str:
    """Generates text based on a prompt using the OpenAI GPT-4 model."""
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    print(text_generation(prompt="meaning of life?"))
