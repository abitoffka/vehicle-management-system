from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Wrong Credentials')
            return redirect('signin')
                
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')

            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                #Login user and redirect to settings page
                user_login = auth.authenticate(username = username, password = password)
                auth.login(request, user_login)

                #Create new Profile for new User
                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, email = email)
                new_profile.save()
                return redirect('index')
        else:
            messages.info(request, 'Passwords does not match')
            return redirect('signup')
    else: 

        return render(request, 'signup.html')