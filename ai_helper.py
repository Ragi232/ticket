import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_ai_suggestion(title, description):
    if not API_KEY or API_KEY == "your_actual_openrouter_key":
        return (
            "AI is not configured yet.\n"
            "Please configure a valid OpenRouter API key in your .env file."
        )

    try:
        client = OpenAI(
            api_key=API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are CampusFlow, a helpful campus IT support assistant. "
                        "Give three short, safe troubleshooting suggestions. "
                        "Never ask users to share passwords or secret information."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Ticket title: {title}\n"
                        f"Ticket description: {description}"
                    )
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as error:
        print("Could not contact the AI service:", error)
        return "AI suggestions are unavailable. Please try again later."