from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime

from home.models import Contact

from django.contrib.auth.models import User  

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name') # request. post is dict # .get is method 
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')    
        
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()
        messages.success(request, 'Profile details updated.')



    return render(request, 'contact.html')

    

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')


def android(request):
    return render(request, 'android.html')

def handlesignup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']


    # Check for errorneous inputs

        # username must be under 10 characters
        if len(username) > 10:
            messages.error(request, 'You cannot enter username more than 10 character')
            return redirect('/')


        #  username must be alphanumeric


        elif not username.isalnum():
            messages.error(request, 'Username must contain only alphanumeric values')
            return redirect('/')

        # 

        if len(mobile) < 10:
            messages.error(request, 'Your Mobile number must be between 10 to 12 numbers')
            return redirect('/')

        
    # Create user

        myuser = User.objects.create_user(username, email, password)
        myuser.name = name
        myuser.save()
        messages.success(request, 'Your account is created')
        return redirect('/')

    else:
        return HttpResponse('404-Not found')


def handlesLogin(request):
    if request.method == 'POST':
        logusername = request.POST['logusername']
        logpassword = request.POST['logpassword']

        user = authenticate(username = logusername, password = logpassword)

        if user is not None:
            login(request, user)
            messages.success(request,'You\'ve logged in Successfully')
            return redirect('/') 
 
        else:
            messages.success(request, 'Invalid Credentials')
            return redirect('/')


    return HttpResponse('404-Not found')

def handlesLogout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('/')
    

 