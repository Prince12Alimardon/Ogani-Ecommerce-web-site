from django.contrib import admin
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class RateInline(admin.TabularInline):
    model = Rate
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, RateInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Rate)
admin.site.register(Product, ProductAdmin)
