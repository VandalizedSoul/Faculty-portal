from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from phonenumber_field.phonenumber import PhoneNumber
# Create your views here.
def index(request):
  designation = request.POST.get('designation','')
  department = request.POST.get('department','')
  image = request.FILES.get('image')
  print("Dataa",designation,department)
  f = Faculty(phone= PhoneNumber.from_string(phone_number="9913419556", region='IN').as_e164,faculty_name="ravi",
        designation="asst. prof.",department="ce",qualifications=[Qualification(degree="U.G.",institute="D.D.U",year=2020),
        Qualification(degree="P.G.",institute="Oxford",year=2024)],email="rv@gmail.com",website="http://www.google.com",
        biography="Velle bethe he",specializations=[Topic(topic_name="Art")],teaching_interests=[Topic(topic_name="big data")],
        publications=[Publication(title="my publication",description="pubblication details",publisher="Vougue India",publication_date="2020-04-01",publication_url="https://www.google.com")],
        awards=[Award(title="award",description="best actor",issuer="filmfare",issue_date="2020-04-01",award_url="https://www.google.com")],
        organizations=[Organization(organization_name="google",position="ceo",description="talented company",duration=40)],
        faculty_type="visiting",image=image)
  f.save()
  faculty = Faculty.objects.filter()
  count = faculty.count()
  return HttpResponse(count)

def addFaculty(request):
  designation = request.POST.get('designation','')
  name = request.POST.get('name','')
  image = request.FILES.get('profile')
  print(image)
  f = Faculty(designation=designation,faculty_name=name,image=image)
  f.save()
  return HttpResponse("saved")

def getAllFaculty(request):
  # faculty = Faculty.objects.filter(faculty_name="ravi",publications={'title':'my publication'})
  faculty = Faculty.objects.filter()
  # print(faculty.count())
  return render(request,'index.html',{'faculty': faculty})

def getFacultyByID(request,faculty_id='ravi'):
  # faculty_id = request.POST.get()
  faculty = Faculty.objects.filter(faculty_name=faculty_id)
  # print(faculty.count())
  return render(request,'index.html',{'faculty': faculty})

def updateFaculty(request):
  faculty_id = request.POST.get('id','')
  faculty = Faculty.objects.filter(faculty_name=faculty_id).update(faculty_type='teaching')
  

