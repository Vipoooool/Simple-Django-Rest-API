from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(["GET"])
def TestFunc(request):
    return Response("API successfully called!")

@api_view(["POST"])
def Weight(height):
    height = json.loads(height.body)
    weight = str(height * 10)
    return JsonResponse("Your weight should be "+weight+"kg!", safe=False)
