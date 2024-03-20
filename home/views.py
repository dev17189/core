from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hom(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')