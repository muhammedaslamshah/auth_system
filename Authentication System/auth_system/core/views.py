from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser=User.objects.create_user(username,email,password)
        myuser.save()

        return redirect('login')


    return render(request, 'register.html')

def loginn(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)

            return redirect('welcome')

        else:
            return redirect('register')
    return render(request, 'login.html')

def welcome(request):
    return render(request, 'welcome.html')