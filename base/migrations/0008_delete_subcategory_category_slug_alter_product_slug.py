# Generated by Django 4.1 on 2022-09-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_subcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=True, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]