from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
# whatever name you have given to a function that same name is of views.
 
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def gaurav(request):
    return HttpResponse('<h1>Gaurav Kumar</h1>')