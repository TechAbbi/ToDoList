from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def Intro(request):
    return HttpResponse("Hello World!")


def index(request):
    return render(request, "todolist/index.html")

