from django.contrib import admin
from .models import Category, Product, Subscription


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('title', ), }


admin.site.register(Subscription)
