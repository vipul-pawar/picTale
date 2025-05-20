from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.
def signup(request):

     if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        # Check for empty fields
        if not uname or not email or not pass1 or not pass2:
            messages.error(request, "All fields are required!")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken! Choose another.")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered! Use another email.")
            return redirect('signup')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email format!")
            return redirect('signup')

        # Check password match
        if pass1 != pass2:
            messages.error(request, "Your password and confirm password do not match!")
            return redirect('signup')
        
        # Save user
        else:

            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()

            messages.success(request, "Account created successfully! You can log in now.")
            return redirect('login')
        



     return render (request,'accounts/signup.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            messages.error(request, "Username or password is incorrect!")
            return redirect('login')

    return render (request,'accounts/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('base')