from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def single_page(request):
    return HttpResponse("hola mundo")

# def index(request):
#     return render(request, "index.html")