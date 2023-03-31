from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is my view, shout out!")
# Create your views here.
