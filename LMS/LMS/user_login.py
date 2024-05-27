from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from app.email_backend import EmailBackend
from django.contrib.auth import login,logout,authenticate

def registerView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if not username or not email or not password:
            messages.error(request,'Username,email and password can\'t be empty!')
        else:
            if User.objects.filter(email=email).exists():
                messages.warning(request,'Email are already exist!')
                return redirect('register')
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username are already exists!')
                return redirect('register')
            user=User(
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()
            messages.success(request,'Account created successfully!')
            return redirect('login')
    return render(request,'registration/register.html')

def loginView(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if not email  or not password:
            messages.error(request,'Email and password can\'t be empty!')
        else:
            user=EmailBackend.authenticate(request,username=email,password=password)
            if user!=None:
                login(request,user)
                messages.success(request,'Log In Successfully!')
                return redirect('home')
            else:
                messages.error(request,'Email and Password are invalid!')
                return redirect('login')
    return render(request,'registration/login.html')

def profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')
    
def profile(request):
    return render(request,'registration/profile.html')
    
def profile_update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')
        