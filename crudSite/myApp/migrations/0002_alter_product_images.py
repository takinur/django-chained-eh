# Generated by Django 4.1 on 2022-09-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.FileField(blank=True, default='photos/products/placeholder.png', upload_to='photos/products'),
        ),
    ]
