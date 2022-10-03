from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
import uuid
import os


class Category(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('categories/', new_filename)

    title = models.CharField(unique=True, max_length=50, db_index=True)
    slug = models.SlugField(unique=True, max_length=100, db_index=True)
    image = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)


class Product(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('products/', new_filename)

    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(unique=True, max_length=100, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to=get_file_name)
    image2 = models.ImageField(upload_to=get_file_name, blank=True)
    image3 = models.ImageField(upload_to=get_file_name, blank=True)
    image4 = models.ImageField(upload_to=get_file_name, blank=True)
    image5 = models.ImageField(upload_to=get_file_name, blank=True)
    trending = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.price}'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('price',)
        index_together = (('id', 'slug'),)


class Subscription(models.Model):
    email_re = RegexValidator(regex=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
                              message='Incorrect email')
    email = models.CharField(max_length=50, validators=[email_re])

    def __str__(self):
        return f'{self.email}'

    class Meta:
        ordering = ('id', )
