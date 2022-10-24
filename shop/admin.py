from django.contrib import admin
# from parler.admin import TranslatableAdmin
from .models import Category, Product
# from parler.admin import TranslatableAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    # def get_prepopulated_fields(self, request, obj=None):
    #     return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    # def get_prepopulated_fields(self, request, obj=None):
    #     return {'slug': ('name',)}
# django-parler doesn’t support the prepopulated_fields attribute, but it
# does support the get_prepopulated_fields() method that provides the same
# functionality. Let’s change this accordingly.