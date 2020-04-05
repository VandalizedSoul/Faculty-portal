from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import datetime
from details.models import *
import time
from twilio.rest import Client


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
            request.session['faculty_id'] = username
            return HttpResponseRedirect('/faculty/show')

        else:
            print("incorrect cred")
            messages.add_message(request, messages.WARNING,
                                 'Incorect Username or Password')
            return HttpResponseRedirect('/login')
    except:
        return render(request, 'login.html')


@login_required()
def logout(request):
    try:
        if request.user.is_authenticated:
            auth.logout(request)
        messages.add_message(request, messages.INFO,
                             'You are Successfully Logged Out')
        messages.add_message(request, messages.INFO, 'Thanks for visiting.')
        # request.session.clear()
        return HttpResponseRedirect('/login/')
    except:
        messages.add_message(request, messages.WARNING,
                             'exception Occured..please try again.')
        return render(request, ' login.html')


def signup(request):
    # c = {}
    # c.update(csrf(request))
    return render(request, 'signup.html', {'sent': False})


def addUser(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    u = User.objects.create_user(username=username, password=password)
    u.save()
    return HttpResponseRedirect("/login")


def generatePassword(request):
    # Download the helper library from https://www.twilio.com/docs/python/install
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    # Your Account SID from twilio.com/console
    account_sid = "AC78c49e25d84d6799db210f8dbcb44e89"
    # Your Auth Token from twilio.com/console
    auth_token = "328b11c7dab1d11c18ad2febf4f37380"

    client = Client(account_sid, auth_token)
    faculty_id = request.POST.get('faculty_id')
    faculty = Faculty.objects.filter(faculty_name='ravi').first()
    # print('faculty',faculty)
    phone = faculty.phone.__str__()
    # message = client.messages.create(
    #     to="+919979779847",
    #     from_="+919913419556",
    #     body="Hello from Ravi!")
    # service = client.verify.services.create(friendly_name='My First Verify Service')
    verification = client.verify.services(
        'VA1d90e5a021ec67fb8ad2473df8cd3c57').verifications.create(to=phone, channel='sms')
    # print(verification.status)

    # print(service.sid)
    # print(message.sid)
    return render(request, 'signup.html', {'sent': True,'faculty_id':'ravi'})


def verify(request):
    account_sid = "AC78c49e25d84d6799db210f8dbcb44e89"
    # Your Auth Token from twilio.com/console
    auth_token = "328b11c7dab1d11c18ad2febf4f37380"
    otp = request.POST.get('otp')
    client = Client(account_sid, auth_token)
    verification_check = client.verify \
                           .services('VA1d90e5a021ec67fb8ad2473df8cd3c57') \
                           .verification_checks \
                           .create(to='+919913419556', code=otp)

    # print(verification_check.status)
    if(verification_check.status=='approved'):
        return HttpResponse("verified")
    return render(request, 'signup.html', {'sent': True,'faculty_id':'ravi','message':'otp not verified!! reenter'})
