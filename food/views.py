from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.
# whatever name you have given to a function that same name is of views.
 
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'food/index.html',context)

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def gaurav(request):
    return HttpResponse('<h1>Gaurav Kumar</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request,'food/detail.html',context)
    # return HttpResponse('This is item no/id: %s' % item_id)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})