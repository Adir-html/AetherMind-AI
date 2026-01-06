from groq import Groq
client = Groq(api_key="YOUR_API_KEY_HERE")


def summarize_chunk(text: str) -> str:
    """Summarize a chunk of text using Groq's Llama 3 model."""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Summarize the following text clearly and concisely."},
                {"role": "user", "content": text}
            ],
            max_tokens=150
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error during summarization: {e}"
