from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.


def homepage(request):
    return render(request, "app/homepage.html")
