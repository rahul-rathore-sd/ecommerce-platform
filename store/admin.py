# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Banner, Categorylogo

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available',)
    search_fields = ('name',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('available',)
    search_fields = ('name',)

@admin.register(Categorylogo)
class CategorylogoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)