from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .services import ask_ai


@require_POST
def chat(request):

    question = request.POST.get(
        "message",
        ""
    ).strip()

    if not question:

        return JsonResponse(
            {
                "reply": "Please type a question."
            }
        )

    answer = ask_ai(question)

    return JsonResponse(
        {
            "reply": answer
        }
    )