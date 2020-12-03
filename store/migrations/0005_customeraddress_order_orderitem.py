# Generated by Django 3.0.9 on 2020-12-01 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_auto_20201201_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField(auto_now_add=True)),
                ('isComplete', models.BooleanField(default=False, null=True)),
                ('orderCustomer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('orderProduct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oiQuantity', models.IntegerField(blank=True, default=0, null=True)),
                ('oiDate', models.DateField(auto_now_add=True)),
                ('oiOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order')),
                ('oiProduct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caProvince', models.CharField(max_length=20, null=True)),
                ('caCity', models.CharField(max_length=50, null=True)),
                ('caAddress', models.CharField(max_length=100, null=True)),
                ('caDate', models.DateField(auto_now_add=True)),
                ('caCustomer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('caOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order')),
            ],
            options={
                'verbose_name_plural': 'Customer Addresses',
            },
        ),
    ]
