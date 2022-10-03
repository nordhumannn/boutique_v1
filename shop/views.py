from django.shortcuts import render, redirect, get_object_or_404
from base.models import Product, Category
from django.core.paginator import Paginator


def product_list(request):
    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.all()

    products_paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    page = products_paginator.get_page(page_num)

    data = {
        'categories': categories,
        'page': page,
        'count': products.count()
    }

    return render(request, 'shop.html', context=data)


def products_in_category(request, slug):
    products = Product.objects.filter(category__slug=slug)
    category_title = Category.objects.filter(slug=slug).first()
    categories = Category.objects.filter(is_visible=True)

    products_paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    page = products_paginator.get_page(page_num)

    data = {
        'page_category': page,
        'category_title': category_title,
        'categories': categories,
        'count': products.count()
    }

    return render(request, 'products_in_category.html', context=data)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_visible=True)
    category_slug = product.category.slug
    related_products = Product.objects.filter(category__slug=category_slug).exclude(slug=product.slug)
    data = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context=data)
