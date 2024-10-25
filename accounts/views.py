from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


user=User
def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'با موفقیت وارد شدید')
            return redirect('/')


    form=AuthenticationForm
    return render(request,'accounts/login.html',{'form':form})

@login_required
def logout_view(request):
    messages.success(request,' شما از سایت خارج شدید')
    logout(request)
    return redirect('/')


def sign_up(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'ثبت نام شما با موفقیت انجام شد')
            return redirect('/')
    form=UserCreationForm
    return render(request,'accounts/signup.html',{'form':form})


