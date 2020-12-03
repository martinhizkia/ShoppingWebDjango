from django.contrib import admin
from django.urls import path 
from .views import * 
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views
   

urlpatterns = [
    path('', homepage, name='page-home'), 
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('account/', user_views.settings, name='account'),
    path('cart/', cart , name='cart'),
    path('checkout/', checkout , name='checkout'),
    path('updateitem/', updateItem, name='update-item'),
    path('product/<int:pk>', detailedView.as_view(), name='product-detailed'),
     path('processorder/', processOrder, name='process-order'),
]
