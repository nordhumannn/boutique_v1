# Generated by Django 4.1 on 2022-09-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
