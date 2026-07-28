from google import genai
from django.conf import settings
from .prompts import SYSTEM_PROMPT
from .context import search_products, serialize

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

def ask_ai(question):
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
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text