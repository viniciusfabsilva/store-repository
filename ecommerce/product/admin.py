from django.contrib import admin
from .models import Product, Category, CustomizationOption


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "availability", "stock")


class CustomizationOptionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "parent")

admin.site.register(Product, ProductAdmin)
admin.site.register(CustomizationOption, CustomizationOptionAdmin)
admin.site.register(Category, CategoryAdmin)
