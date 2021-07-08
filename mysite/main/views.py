from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Hello from homepage!")
    


def test(request):
    return render(request, 'index.html')