from django.contrib import admin
from .models import Category, Product, MyDashApp

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'brand']
    list_filter = ['name', 'created', 'updated']
    list_editable = ['slug', 'category', 'brand']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(MyDashApp)
