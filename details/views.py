from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from phonenumber_field.phonenumber import PhoneNumber
# Create your views here.
def index(request):
  f= Faculty(phone= PhoneNumber.from_string(phone_number="9913419556", region='RU').as_e164,faculty_name="ravi",designation="asst. prof.",department="ce",qualifications=[Qualification(degree="U.G.",institute="D.D.U",year=2020),Qualification(degree="P.G.",institute="Oxford",year=2024)],email="rv@gmail.com",website="http://www.google.com",biography="Velle bethe he",specializations=[Topic(topic_name="Art")],teaching_interests=[Topic(topic_name="big data")])
  f.save()
  faculty = Faculty.objects.filter()
  count = faculty.count()
  return HttpResponse(count)