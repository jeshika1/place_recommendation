from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserPreference


def home(request):
    return render(request, "index.html")

@csrf_exempt  # We’ll fix CSRF later
def save_preferences(request):
    if request.method == "POST":
        data = json.loads(request.body)

        UserPreference.objects.create(
            budget=data.get("budget"),
            food_type=data.get("food"),
            people=data.get("people"),
            location=data.get("location"),
            vibe=data.get("vibe"),
            cuisine=data.get("cuisine"),
            extra=data.get("extra")
        )

        return JsonResponse({"message": "Data saved successfully"})
    return JsonResponse({"message": "Invalid request"}, status=400)
