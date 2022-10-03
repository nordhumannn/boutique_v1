import email
from email.policy import default
from django.db import models
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


class OrderCheckout(models.Model):

    email_re = RegexValidator(
        regex=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
        message='Incorrect email'
    )

    phone_number_re = RegexValidator(
        regex=r"^(\d{3}[- .]?){2}\d{4}$",
        message='Incorrect phone number (xxx xxx xxxx)'
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, validators=[email_re])
    phone_number = models.CharField(max_length=13, validators=[phone_number_re])
    company_name = models.CharField(max_length=50, blank=True)
    country = CountryField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self) -> str:
        return f'Order: {self.id}, paid: {self.paid}'
