
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm , CustomerReg
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from reg.models import Customer
# Create your views here.
def Sign_up(request):
    if request.method == 'POST':
        fm= SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render (request, 'reg/signup.html',{'form':fm})


#Login View
def User_login(request):
    if  not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'reg/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
        
def User_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fmm = CustomerReg(request.POST)
            if fmm.is_valid():
                nm = fmm.cleaned_data['name']
                em = fmm.cleaned_data['email']
                ct = fmm.cleaned_data['city']
                reg = Customer( name=nm,email=em,city=ct)
                reg.save()
                fmm = CustomerReg()
        else:
            fmm = CustomerReg()
        cust = Customer.objects.all()
        return render(request, 'reg/profile.html',{'name':request.user, 'formm':fmm, 'stu':cust})
    else:
        return HttpResponseRedirect('/login/')


def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# This function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = Customer.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/profile/')

# This function will update
def update_data(request, id):
    if request.method == 'POST':
        pi = Customer.objects.get(pk = id)
        fmm = CustomerReg(request.POST, instance=pi)
        if fmm.is_valid():
            fmm.save()
    else:
        pi = Customer.objects.get(pk=id)
        fmm = CustomerReg(instance=pi)        
    return render(request, 'reg/updatecustomer.html',{'formm':fmm})




