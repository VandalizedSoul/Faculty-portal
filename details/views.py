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

from .models import Faculty



#
# class FacultyDetails(generic.ListView):
#     model = Faculty
#     context_object_name = 'faculty'
#     template_name = 'facultydetails.html'

from django.shortcuts import redirect
from .forms import *


def updateimage(request,faculty_id):
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
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = AboutForm
    success_message = 'Success: About was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class CertificationUpdateView(BSModalUpdateView):
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
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = TeachingInterestForm
    success_message = 'Success: Teaching Interest was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class SpecializationUpdateView(BSModalUpdateView):
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = SpecializationForm
    success_message = 'Success: Specialization was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class OrganizationUpdateView(BSModalUpdateView):
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
    model = Faculty
    template_name = 'read_qualification.html'


# Delete Views
class QualificationDeleteView(BSModalDeleteView):
    model = Qualification
    template_name = 'delete_qualification.html'
    success_message = 'Success: Qualification was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class OrganizationDeleteView(BSModalDeleteView):
    model = Organization
    template_name = 'delete_qualification.html'
    success_message = 'Success: Organization was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class CertificationDeleteView(BSModalDeleteView):
    model = Certification
    template_name = 'delete_qualification.html'
    success_message = 'Success: Certification was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AwardDeleteView(BSModalDeleteView):
    model = Award
    template_name = 'delete_qualification.html'
    success_message = 'Success: Award was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class PublicationDeleteView(BSModalDeleteView):
    model = Publication
    template_name = 'delete_qualification.html'
    success_message = 'Success: Publication was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


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
    print("faculty: ",faculty_id)

    faculty = Faculty.objects.get(faculty_id=faculty_id)
    qualification = Qualification.objects.all().filter(faculty=faculty)
    publication = Publication.objects.all().filter(faculty=faculty)
    award = Award.objects.all().filter(faculty=faculty)
    organization = Organization.objects.all().filter(faculty=faculty)
    certification = Certification.objects.all().filter(faculty=faculty)
    if qualification:
        latest_qualification = Qualification.objects.all().filter(faculty=faculty).latest('to_year')
    else:
        latest_qualification=None
    print('latest Q',latest_qualification)
    print(qualification, 'q')
    login_faculty_id = request.session.get('faculty_id', None)
    #
    # context = {'faculty': faculty,'login_faculty':login_faculty_id}
    if(login_faculty_id==faculty.faculty_id):
        print("same login")
    # login_faculty_id=True
    print("ID's",login_faculty_id,faculty.faculty_id)
    context = {'faculty': faculty, 'qualifications': qualification, 'publications': publication, 'awards': award, 'organizations': organization, 'certifications': certification, 'latest_qualification': latest_qualification,'login_faculty_id':login_faculty_id}
    return render_to_response('facultydetails.html', context)


def invalidlogin(request):
    return render_to_response('invalidlogin.html')



def home(request):
    # auth.logout(request)
    faculties = Faculty.objects.filter()
    login_faculty_id = request.session.get('faculty_id', None)
    return render_to_response('home.html', {"faculties": faculties,login_faculty_id:login_faculty_id})