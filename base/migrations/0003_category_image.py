# Generated by Django 4.1 on 2022-09-08 13:59

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=123, upload_to=base.models.Category.get_file_name),
            preserve_default=False,
        ),
    ]
