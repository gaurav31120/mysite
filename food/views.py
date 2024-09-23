from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# whatever name you is given to a function that same name is of views.
 
def index(request):
    return HttpResponse('Hello World')
