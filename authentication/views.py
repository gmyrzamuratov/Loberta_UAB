from django.shortcuts import render, redirect
from authentication.models import User
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.
def signin(request):

    return render(request, "authentication/signin.html")

def signup(request):

    return render(request, "authentication/signup.html")

def login(request):

    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('links:index')
    else:
        error = {'message': 'Incorrect user or password', }
        return render(request, "authentication/signin.html", error)

def registration(request):

    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:

        user = User(email=email)
        user.set_password(password)
        user.is_active = True
        user.save()

        return redirect('links:index')
    else:
        error = {'message': 'Password does not same', }
        return render(request, "authentication/signup.html", error)
