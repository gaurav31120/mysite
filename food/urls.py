from . import views
from django.urls import path


urlpatterns = [
    path('food/', views.index,name='index'),
]

