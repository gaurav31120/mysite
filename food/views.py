from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# whatever name you have given to a function that same name is of views.
 
def index(request):
    return HttpResponse('Hello World')

def item(request):
    return HttpResponse('This is an item view')

def gaurav(request):
    return HttpResponse('<h1>Gaurav Kumar</h2>')