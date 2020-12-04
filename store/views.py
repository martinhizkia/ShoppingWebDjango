from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Q
from django.core.paginator import Paginator


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
    p = Paginator(products, 6)
    page_num = request.GET.get('page',1)
    page = p.page(page_num)
    context = {'products': page, 'cartItems':cartItems}
    return render(request, 'store/home.html',context)

class detailedView(DetailView):
    model = Product
    template_name = 'store/detailed.html'

class categorylist(ListView):
    model = Product
    context_object_name = 'categories'
    cats = Category.objects.all()
    template_name = 'store/category.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(categorylist, self).get_context_data( *args, **kwargs)
        context['cat_menu'] = cat_menu
        return context



def product_category(request):
    context = {
        "categories": Category,
    }
    return render(request,"store/category.html",context)

class searchView(ListView):
    model = Product
    context_object_name = 'all_search_results'
    template_name = 'store/search.html'
    
    def get_queryset(self):
        result = super(searchView, self).get_queryset()
        query = self.request.GET.get('search')
        print(query)
        sss = (Q(productName__icontains=query))
        if query:
            postresult = Product.objects.filter(sss)
            result = postresult
        else:
            result = None
        return result

def category(request, category_name):
    products = Product.objects.filter(productCategory__name = category_name)
    return render(request, 'store/categorical.html', {'category_name':category_name, 'products':products})


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
        order.isComplete = True
        order.save()
    return JsonResponse("Terima Kasih Telah Berbelaja", safe=False)

@login_required
def processdone(request):
    return render(request, 'store/processorder.html')

@login_required
def history(request):
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.all().filter(orderCustomer=customer, isComplete=True)
    else:
        order= {"get_total_price":0, "get_total_item": 0}
    context = {'orders': order}#'items': items,
    return render(request, 'store/history.html', context)