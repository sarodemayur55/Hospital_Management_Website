from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("User logged in")
            messages.info(request, "Logged In Successfullly")
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')




def register(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in!!!")
        return redirect('/')
    print("Page requested")
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                print('User taken')
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username, password=password1, first_name=firstname, last_name=lastname)
                user.save()
                messages.info(request, 'User Created')
                print("User Created")
        else:
            print("password not matching")
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')