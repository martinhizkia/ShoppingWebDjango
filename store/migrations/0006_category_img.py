# Generated by Django 3.0.9 on 2020-12-04 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customeraddress_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.URLField(blank=True, max_length=600, null=True),
        ),
    ]