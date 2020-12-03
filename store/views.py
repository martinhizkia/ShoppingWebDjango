from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
class homeView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = "products"

def homepage(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(orderCustomer=customer, isComplete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_item
    else:
        items = []
        order = {"get_total_price":0, "get_total_item": 0}
        cartItems = order['get_total_item']

    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'store/home.html',context)

class detailedView(DetailView):
    model = Product
    template_name = 'store/detailed.html'

@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(orderCustomer=customer, isComplete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order= {"get_total_price":0, "get_total_item": 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)

@login_required
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(orderCustomer=customer, isComplete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_total_price":0, "get_total_item": 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)

@login_required
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(productId)
    print(action)
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(orderCustomer=customer, isComplete=False)
    orderItem, created = OrderItem.objects.get_or_create(oiOrder=order, oiProduct=product)

    if action == 'add':
        orderItem.oiQuantity += 1
    elif action == 'remove':
        orderItem.oiQuantity -= 1

    orderItem.save()

    if orderItem.oiQuantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was Added', safe=False)

@login_required
def processOrder(request):
    data = json.loads(request.body)
    customer = request.user
    print("---------------------",data,"-----------------")
    order, created = Order.objects.get_or_create(orderCustomer=customer, isComplete=False)
    if request.user == order.orderCustomer:
        CustomerAddress.objects.create(
        caCustomer = request.user,
        caOrder = order,
        caProvince = data['alamatPengiriman']['province'],
        caCity = data['alamatPengiriman']['city'],
        caAddress = data['alamatPengiriman']['address'])
    return JsonResponse("Terima Kasih Telah Berbelaja", safe=False)