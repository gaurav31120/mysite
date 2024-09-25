from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# whatever name you have given to a function that same name is of views.
 
def index(request):
    return HttpResponse('Hello World')
