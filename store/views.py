# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import Product, Banner, Categorylogo

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store/product_list.html', {'products': products})

def home(request):
        banners = Banner.objects.all() 
        images = Categorylogo.objects.all()
        context = {
            #   'banners': banners,
              'images': images
        }
        return render(request, "store/home.html", context)