# Generated by Django 3.0.9 on 2020-12-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201201_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productPrice',
            field=models.IntegerField(),
        ),
    ]
