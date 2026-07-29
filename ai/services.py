from google import genai
from django.conf import settings

from .prompts import SYSTEM_PROMPT
from .context import search_products, serialize


def ask_ai(question: str) -> str | None:
    """
    Ask Gemini using marketplace context.
    """

    if not settings.GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured. "
            "Add it to your Vercel Environment Variables."
        )

    client = genai.Client(api_key=settings.GEMINI_API_KEY)

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
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text