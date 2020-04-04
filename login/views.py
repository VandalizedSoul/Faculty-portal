from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import datetime
from details.models import *

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)
  
def auth_view(request):
    try:
        if request.user.is_authenticated:
            '''if request.user.is_superuser:
                return render(request,' index.html')'''
            return HttpResponseRedirect('/faculty/show')

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("logged in")
            return HttpResponseRedirect('/faculty/show')    
            
        else:
            print("incorrect cred")
            messages.add_message(request, messages.WARNING, 'Incorect Username or Password')
            return HttpResponseRedirect('/faculty/show')
    except:
        return render(request,'login.html')


@login_required()
def logout(request):
    try:
        if request.user.is_authenticated:
            auth.logout(request)
        messages.add_message(request, messages.INFO, 'You are Successfully Logged Out')
        messages.add_message(request, messages.INFO, 'Thanks for visiting.')
        #request.session.clear()
        return HttpResponseRedirect('/login/')
    except:
        messages.add_message(request, messages.WARNING, 'exception Occured..please try again.')
        return render(request,' login.html')

def signup(request):
    c = {}
    c.update(csrf(request))
    return render(request,'signup.html', c)

def addUser(request):
    username = request.POST.get('username', '')
    password= request.POST.get('password', '')
    u = User.objects.create_user(username = username, password = password)
    u.save()
    return HttpResponseRedirect("/login")

def generatePassword(request):
    pass