from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
# whatever name you have given to a function that same name is of views.
 
def index(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)

def item(request):
    return HttpResponse('This is an item view')

def gaurav(request):
    return HttpResponse('<h1>Gaurav Kumar</h2>')