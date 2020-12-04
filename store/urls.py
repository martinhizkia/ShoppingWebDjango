from django.contrib import admin
from django.urls import path, include
from .views import * 
from django.conf.urls.static import static
from users import views as user_views
from users.views import *
from django.contrib.auth import views as auth_views

   

urlpatterns = [
    path('', homepage, name='page-home'), 
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('accountprofile/', user_views.profile, name='profile'),
    #path('updateaccount/', include('django.contrib.auth.urls')),
    path('account/password/', auth_views.PasswordChangeView.as_view(template_name='users/changepassword.html',  success_url = reverse_lazy('passworddone')), name='password'),
    path('account/password/success', auth_views.PasswordChangeDoneView.as_view(template_name='users/donepassword.html',), name='passworddone'),
    path('account/', user_views.settings, name='account'),
    path('cart/', cart , name='cart'),
    path('category/<str:category_name>', category, name='category'),
    path('category/', categorylist.as_view(), name='catlist'),
    path('checkout/', checkout , name='checkout'),
    path('updateitem/', updateItem, name='update-item'),
    path('search/', searchView.as_view(), name='search-item'),
    path('account/history', history, name='order-history'),
    path('product/<int:pk>', detailedView.as_view(), name='product-detailed'),
    path('processorder/', processOrder, name='process-order'),
     path('processorder/done', processdone, name='process-done')
]
