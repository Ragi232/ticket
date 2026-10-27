import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_ai_suggestion(title, description):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return (
            "API key not found. Open your .env file and check "
            "OPENROUTER_API_KEY."
        )

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful student IT support assistant. "
                        "Give clear, simple, safe troubleshooting steps."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Ticket title: {title}\n"
                        f"Description: {description}\n"
                        "Suggest steps to solve this problem."
                    )
                }
            ]
        )

        return (
            response.choices[0].message.content
            or "The AI did not return a suggestion."
        )

    except Exception as error:
        return f"AI request failed: {error}"