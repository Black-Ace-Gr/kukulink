from google import genai
from django.conf import settings

from .prompts import SYSTEM_PROMPT
from .context import search_products, serialize


def get_client():
    """
    Lazily create the Gemini client so the application
    can start even if the AI endpoint isn't used.
    """
    if not settings.GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY environment variable is not set."
        )

    return genai.Client(api_key=settings.GEMINI_API_KEY)


def ask_ai(question):
    client = get_client()

    products = search_products(question)
    context = serialize(products)

    prompt = f"""
{SYSTEM_PROMPT}

Marketplace Data

{context}

Question

{question}

Answer using the marketplace data whenever possible.

If no marketplace data answers the question,
answer using poultry knowledge.

Never invent products that do not exist.
"""

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt,
    )

    return response.text