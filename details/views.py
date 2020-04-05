# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

from details.models import Faculty


def getstudentinfo(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('addstudentinfo.html', c)


def addinfo(request):
    # sname = request.POST.get('organization_name', '')
    # sposition = request.POST.get('position', '')
    # s = Faculty()
    # s.save()
    c = {}
    c.update(csrf(request))
    return render_to_response('addinfo.html', c)
    # return HttpResponseRedirect('/polls/facultydetails/')

#
# def addsuccess(request):
#     return render_to_response('addrecord.html')


class StudentListView(generic.ListView):
    model = Faculty


def index(request):
    return HttpResponse("hello World!! Django is unchained!")


# class HomePageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html', context=None)


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,
    password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/details/facultydetails/')
    else:
        return HttpResponseRedirect('/polls/invalidlogin/')


def facultydetails(request):
    return render_to_response('facultydetails.html', {"full_name":request.user.username})


def invalidlogin(request):
    return render_to_response('invalidlogin.html')


def home(request):
    auth.logout(request)
    return render_to_response('logout.html')