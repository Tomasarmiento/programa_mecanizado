from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, "index.html")

def vf4(request):
    return render(request, "vf4.html")

def vf2(request):
    return render(request, "vf2.html")

def st35(request):
    return render(request, "st35.html")

def laser(request):
    return render(request, "laser.html")