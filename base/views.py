from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Product
from .forms import SubscriptionForm


def base(request):

    if request.method == 'POST':
        subscription = SubscriptionForm(request.POST)
        if subscription.is_valid():
            subscription.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    products = Product.objects.filter(is_visible=True)
    trending = Product.objects.filter(trending=True)
    subscription = SubscriptionForm()

    data = {
        'categories': categories,
        'products': products,
        'trending': trending,
        'subscription_form': subscription,
    }

    return render(request, 'base.html', context=data)
