# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render
from django.template import RequestContext
from django.views import generic
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import QualificationForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Faculty

from details.models import Faculty



#
# class FacultyDetails(generic.ListView):
#     model = Faculty
#     context_object_name = 'faculty'
#     template_name = 'facultydetails.html'

from django.shortcuts import redirect
from details.forms import *


def updateImage(request,faculty_id):
    faculty_id = request.POST.get('id', '')
    faculty = Faculty.objects.get(faculty_id=faculty_id)
    context = {'faculty': faculty}
    image = request.FILES.get('image')
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(image=image)

    return render(request,'facultydetails.html',context)


def deleteImage(request):
    faculty_id = request.POST.get('id', '')
    image = 'Default Image URL'
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(image=image)
    return HttpResponse('saved')




def profile_image_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render_to_response('facultydetails.html', context_instance=RequestContext(request))
    else:
        form = ProfileForm()
    return render(request, 'profile_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')




class QualificationCreateView(BSModalCreateView):
    template_name = 'create_qualification.html'
    form_class = QualificationForm
    success_message = 'Success: Qualification was created.'
    success_url = reverse_lazy('facultydetails')


class QualificationUpdateView(BSModalUpdateView):
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = QualificationForm
    success_message = 'Success: Qualification was updated.'
    success_url = reverse_lazy('facultydetails')


class QualificationReadView(BSModalReadView):
    model = Faculty
    template_name = 'read_qualification.html'


class QualificationDeleteView(BSModalDeleteView):
    model = Faculty
    template_name = 'delete_qualification.html'
    success_message = 'Success: Qualification was deleted.'
    success_url = reverse_lazy('facultydetails')




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

#


#
# def auth_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username,
#     password=password)
#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect('/polls/facultydetails/')
#     else:
#         return HttpResponseRedirect('/polls/invalidlogin/')



def facultydetails(request, faculty_id):
    # faculty_id = request.GET.get('id')
    print(faculty_id)
    faculty = Faculty.objects.get(faculty_id=faculty_id)
    context = {'faculty': faculty}
    return render_to_response('facultydetails.html', context)


def invalidlogin(request):
    return render_to_response('invalidlogin.html')



def home(request):
    # auth.logout(request)
    faculties = Faculty.objects.filter()
    return render_to_response('home.html', {"faculties": faculties})