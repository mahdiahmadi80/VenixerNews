from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from .models import Contact
def index(request):

    return render(request,'website/index.html')

def about(request):

    return render(request,'website/about.html')

def contact(request):
    
    # if request.method == 'POST':
    #     form=ContactForm(request.POST)
    #     if form.is_valid():
    #         name=form.cleaned_data['name']
    #         email=form.cleaned_data['email']
    #         subject=form.cleaned_data['subject']
    #         message=form.cleaned_data['message']
    #         c=Contact()
    #         c.name=name
    #         c.email=email
    #         c.subject=subject
    #         c.message=message
    #         c.save()
    #         return redirect('/')
    
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,' پیام شما ارسال شد')
            return redirect('/')
        else:
            print (form.errors)
    
    
    form=ContactForm()
    return render(request,'website/contact.html',{'form':form})