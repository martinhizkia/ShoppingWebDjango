# Generated by Django 3.0.9 on 2020-12-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201201_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productDesc',
            field=models.CharField(max_length=600),
        ),
    ]