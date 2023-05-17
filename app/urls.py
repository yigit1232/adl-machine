from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('urunler/',views.products,name='products'),
    path('kalite/',views.quality,name='quality'),
]
