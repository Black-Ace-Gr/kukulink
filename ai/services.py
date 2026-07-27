from google import genai
from django.conf import settings
from .prompts import SYSTEM_PROMPT


def ask_ai(question):
    try:
        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[
                SYSTEM_PROMPT,
                question,
            ],
        )

        return response.text

    except Exception as e:
        print(e)
        return (
            "Sorry, Kuku AI is temporarily unavailable. "
            "Please try again in a moment."
        )