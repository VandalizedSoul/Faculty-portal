# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render
from django.template import RequestContext
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import QualificationForm, CustomUserCreationForm, CustomAuthenticationForm, PublicationForm, AwardForm,\
    CertificationForm, OrganizationForm, TeachingInterestForm, SpecializationForm, AboutForm, ProfileForm
from .models import Faculty

from django.shortcuts import redirect
from .forms import *


def facultydetails(request, faculty_id):
    # faculty_id = request.GET.get('id')
    print(faculty_id)
    faculty = Faculty.objects.get(faculty_id=faculty_id)
    qualification = Qualification.objects.all().filter(faculty=faculty)
    publication = Publication.objects.all().filter(faculty=faculty)
    award = Award.objects.all().filter(faculty=faculty)
    organization = Organization.objects.all().filter(faculty=faculty)
    certification = Certification.objects.all().filter(faculty=faculty)
    latest_qualification = Qualification.objects.latest('to_year')
    print('latest Q',latest_qualification)
    print(qualification, 'q')
    context = {'faculty': faculty, 'qualifications': qualification, 'publications': publication, 'awards': award, 'organizations': organization, 'certifications': certification, 'latest_qualification': latest_qualification}
    context.update(csrf(request))
    return render_to_response('facultydetails.html', context)


def invalidlogin(request):
    return render_to_response('invalidlogin.html')

def home(request):
    # auth.logout(request)
    faculties = Faculty.objects.filter()
    return render(request,'home.html', {"faculties": faculties})

@login_required
def changeImage(request):
    faculty_id = request.POST.get('faculty_id', '')
    image = request.FILES['profile']
    print('image post',image)
    faculty = Faculty.objects.filter(faculty_id=faculty_id).first()
    faculty.image = image
    faculty.save()
    print("image after save",faculty.image)
    # handle_uploaded_file(faculty_id,image)  
    # faculty = Faculty.objects.filter(
    #     faculty_name=faculty_id).update(image=image)
    return HttpResponseRedirect('/polls/facultydetails/'+faculty_id+'/')

@login_required
def deleteImage(request):
    faculty_id = request.POST.get('id', '')
    image = None
    faculty = Faculty.objects.filter(faculty_id=faculty_id)
    faculty.image = image
    faculty.save()
    return HttpResponseRedirect('/polls/facultydetails/'+faculty_id+'/')


def success(request):
    return HttpResponse('successfully uploaded')

class QualificationCreateView(BSModalCreateView):
    login_required = True   
    form_class = QualificationForm
    template_name = 'create_qualification.html'
    success_message = 'Success: Qualification was created.'

    def get_form_kwargs(self):
        kwargs = super(QualificationCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        print('request', self.request.session.get('faculty_id', None))
        return kwargs

    def get_success_url (self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class CertificationCreateView(BSModalCreateView):
    login_required = True
    template_name = 'create_qualification.html'
    form_class = CertificationForm
    success_message = 'Success: Certification was created.'

    def get_form_kwargs(self):
        kwargs = super(CertificationCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class PublicationCreateView(BSModalCreateView):
    login_required = True
    template_name = 'create_qualification.html'
    form_class = PublicationForm
    success_message = 'Success: Publication was created.'

    def get_form_kwargs(self):
        kwargs = super(PublicationCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AwardCreateView(BSModalCreateView):
    login_required = True
    template_name = 'create_qualification.html'
    form_class = AwardForm
    success_message = 'Success: Award was created.'

    def get_form_kwargs(self):
        kwargs = super(AwardCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class OrganizationCreateView(BSModalCreateView):
    login_required = True
    template_name = 'create_qualification.html'
    form_class = OrganizationForm
    success_message = 'Success: Organization was created.'

    def get_form_kwargs(self):
        kwargs = super(OrganizationCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


# update views
class QualificationUpdateView(BSModalUpdateView):
    login_required = True
    model = Qualification
    template_name = 'update_qualification.html'
    form_class = QualificationForm
    success_message = 'Success: Qualification was updated.'

    def get_form_kwargs(self):
        kwargs = super(QualificationUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AboutUpdateView(BSModalUpdateView):
    login_required = True
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = AboutForm
    success_message = 'Success: About was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class CertificationUpdateView(BSModalUpdateView):
    login_required = True
    model = Certification
    template_name = 'update_qualification.html'
    form_class = CertificationForm
    success_message = 'Success: Certification was updated.'

    def get_form_kwargs(self):
        kwargs = super(CertificationUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AwardUpdateView(BSModalUpdateView):
    login_required = True
    model = Award
    template_name = 'update_qualification.html'
    form_class = AwardForm
    success_message = 'Success: Certification was updated.'

    def get_form_kwargs(self):
        kwargs = super(AwardUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class PublicationUpdateView(BSModalUpdateView):
    login_required = True
    model = ProfileForm
    template_name = 'update_qualification.html'
    form_class = PublicationForm
    success_message = 'Success: Certification was updated.'

    def get_form_kwargs(self):
        kwargs = super(PublicationUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class TeachingInterestUpdateView(BSModalUpdateView):
    login_required = True
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = TeachingInterestForm
    success_message = 'Success: Teaching Interest was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class SpecializationUpdateView(BSModalUpdateView):
    login_required = True
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = SpecializationForm
    success_message = 'Success: Specialization was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class OrganizationUpdateView(BSModalUpdateView):
    login_required = True
    model = Organization
    template_name = 'update_qualification.html'
    form_class = OrganizationForm
    success_message = 'Success: Organization was updated.'

    def get_form_kwargs(self):
        kwargs = super(OrganizationUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class QualificationReadView(BSModalReadView):
    login_required = True
    model = Faculty
    template_name = 'read_qualification.html'


# Delete Views
class QualificationDeleteView(BSModalDeleteView):
    login_required = True
    model = Qualification
    template_name = 'delete_qualification.html'
    success_message = 'Success: Qualification was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class OrganizationDeleteView(BSModalDeleteView):
    login_required = True
    model = Organization
    template_name = 'delete_qualification.html'
    success_message = 'Success: Organization was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class CertificationDeleteView(BSModalDeleteView):
    login_required = True
    model = Certification
    template_name = 'delete_qualification.html'
    success_message = 'Success: Certification was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AwardDeleteView(BSModalDeleteView):
    login_required = True
    model = Award
    template_name = 'delete_qualification.html'
    success_message = 'Success: Award was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class PublicationDeleteView(BSModalDeleteView):
    login_required = True
    model = Publication
    template_name = 'delete_qualification.html'
    success_message = 'Success: Publication was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


def getstudentinfo(request):
    c = {}
    c.update(csrf(request))
    return render(request,'addstudentinfo.html', c)


def addinfo(request):
    # sname = request.POST.get('organization_name', '')
    # sposition = request.POST.get('position', '')
    # s = Faculty()
    # s.save()
    c = {}
    c.update(csrf(request))
    return render(request,'addinfo.html', c)
    # return HttpResponseRedirect('/polls/facultydetails/')


class StudentListView(generic.ListView):
    model = Faculty

