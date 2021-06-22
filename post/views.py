from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def post(request):
    return JsonResponse({'hell': 'world'})
