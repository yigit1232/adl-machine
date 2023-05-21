from django.shortcuts import render
from .data import get_images
def index(request):
    return render(request,'index.html')

def products(request):
    images = get_images()
    return render(request, 'products.html',{'images':images})
def quality(request):
    return render(request, 'quality.html')

def contact(request):
    return render(request, 'contact.html')

def production(request):
    return render(request,'production.html')