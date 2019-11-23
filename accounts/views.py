from django.shortcuts import render,redirect

# Create your views here.

from django import forms
from .forms import Registerform
#from django.contrib import messages



def register_page(request):
    if request.method=='POST':

        
        form=Registerform(request.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            #messages.success(request,f'account created for {username}!')
            return redirect('login')
    else:
        form=Registerform()
    return render(request,'register.html',{'form':form})