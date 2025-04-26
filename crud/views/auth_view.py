from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login as auth_login

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')
        
    return render(request,'auth/register.html')
def login(request):
    if request.method == 'POST':    
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user) #session establish
            return redirect('home')
        else:
            return redirect('login')
    

    return render(request,'auth/login.html')