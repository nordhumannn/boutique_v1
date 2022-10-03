from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'type': 'email',
            'placeholder': 'Enter your email address',
            'aria-describedby': 'button-addon2',
        })
    )

    class Meta:
        model = Subscription
        fields = ('email',)
