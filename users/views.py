from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun {username} Berhasil Dibuat. Silahkan Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Akun Anda Sudah Terupdate!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html',{"u_form":u_form})

@login_required
def settings(request):
    return render(request, 'users/account.html')

#class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeView
    #template_name = 'users/changepassword.html'
    #success_url = reverse_lazy('account')

