from dataclasses import field
from django import forms
from .models import OrderCheckout
from django_countries.widgets import CountrySelectWidget


class OrderCheckoutForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':'form-control form-control-lg', 
            'type':'text',
            'id':'firstName', 
            'placeholder':'Enter your first name'
        })
    )

    last_name = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'type': 'text',
            'id': 'lastName',
            'placeholder': 'Enter your last name'
        })
    )

    email = forms.EmailField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'type': 'email',
            'id': 'email',
            'placeholder': 'e.g. Jason@example.com'
        })
    )

    phone_number = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'type': 'tel',
            'id': 'phone',
            'placeholder': 'e.g. +022 453 5474'
        })
    )

    company_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'type': 'text',
            'id': 'company',
            'placeholder': 'Your company name'
        })
    )

    country = CountrySelectWidget()

    city = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'type': 'text',
            'id': 'city',
        })
    )

    address = forms.CharField(
        max_length=70,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'type': 'text',
            'id': 'address',
            'placeholder': 'House number and street name'
        })
    )

    class Meta:
        model = OrderCheckout
        fields = ('first_name', 'last_name', 'country', 'email', 'phone_number', 'company_name', 'city', 'address')
