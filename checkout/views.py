from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderCheckoutForm


def checkout_view(request):
    if request.method == 'POST':
        checkout = OrderCheckoutForm(request.POST)
        if checkout.is_valid():
            checkout.save()
            cart = Cart(request)
            cart.clear()
            return render(request, 'checkout_done.html')

    cart = Cart(request)
    checkout = OrderCheckoutForm()
    data = {
        'cart': cart,
        'checkout': checkout
    }
    return render(request, 'checkout.html', context=data)

