from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from phonenumber_field.phonenumber import PhoneNumber
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    designation = request.POST.get('designation', '')
    department = request.POST.get('department', '')
    image = request.FILES.get('image')
    print("Dataa", designation, department)
    f = Faculty(faculty_id='16CE001', phone=PhoneNumber.from_string(phone_number="9913419556", region='IN').as_e164, faculty_name="ravi",
                designation="asst. prof.", department="ce", qualifications=[Qualification(degree="U.G.", institute="D.D.U", from_year=2020, to_year=2020),
                                                                            Qualification(degree="P.G.", institute="Oxford",  from_year=2020, to_year=2020)], email="rv@gmail.com", website="http://www.google.com",
                biography="Velle bethe he", specializations=[Topic(topic_name="Art")], teaching_interests=[Topic(topic_name="big data")],
                publications=[Publication(title="my publication", description="pubblication details",
                                          publisher="Vougue India", publication_date="2020-04-01", publication_url="https://www.google.com")],
                awards=[Award(title="award", description="best actor", issuer="filmfare",
                              issue_date="2020-04-01", award_url="https://www.google.com")],
                organizations=[Organization(
                    organization_name="google", position="ceo", description="talented company", emp_type='idk', location='dkkj', from_date='2020-08-06', to_date='2020-08-06', is_currently_working=False)],
                faculty_type="visiting", image=image, accomplishments=[Topic(topic_name="Accomp")])
    f.save()
    faculty = Faculty.objects.filter()
    count = faculty.count()
    return HttpResponse(count)


def addFaculty(request):
    designation = request.POST.get('designation', '')
    name = request.POST.get('name', '')
    image = request.FILES.get('profile')
    print(image)
    f = Faculty(designation=designation, faculty_name=name, image=image)
    f.save()
    return HttpResponse("saved")


def getAllFaculty(request):
    # faculty = Faculty.objects.filter(faculty_name="ravi",publications={'title':'my publication'})
    faculty = Faculty.objects.filter(faculty_id='16CE001').first()
    # print(faculty.count())
    return render(request, 'index.html', {'faculty': faculty})


def getFacultyByID(request, faculty_id='16CE001'):
    # faculty_id = request.POST.get()
    faculty = Faculty.objects.filter(faculty_name=faculty_id).first()
    url = '/static/profile/'+faculty.faculty_id
    fs = FileSystemStorage()
    if not(fs.exists(url)):
        url = '/static/profile/NoImage.png'
    # print(faculty.count())
    return render(request, 'index.html', {'faculty': faculty,'url':url})

# def updateFaculty(request):
#   faculty_id = request.POST.get('id','')
#   faculty = request.POST.get('faculty')
#   faculty = Faculty.objects.filter(faculty_name=faculty_id).update(faculty_name='ravi')
# def handle_uploaded_file(faculty_id,f):  
#     with open('details/static/profile/'+faculty_id+'.jpg', 'wb+') as destination:  
#         for chunk in f.chunks():  
#             destination.write(chunk)  

def updateImage(request):
    faculty_id = request.POST.get('faculty_id', '')
    image = request.FILES['profile']
    print('image',image)
    faculty = Faculty.objects.filter(
        faculty_id=faculty_id).first()
    faculty.image = image
    faculty.save()
    # handle_uploaded_file(faculty_id,image)  
    # faculty = Faculty.objects.filter(
    #     faculty_name=faculty_id).update(image=image)
    return HttpResponse('image saved')

def deleteImage(request):
    faculty_id = request.POST.get('id', '')
    image = 'Default Image URL'
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(image=image)
    return HttpResponse('saved')


def updateDesignation(request):
    faculty_id = request.POST.get('id', '')
    designation = request.POST.get('designation', '')
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(designation=designation)
    return HttpResponse('saved')


def updateDepartment(request):
    faculty_id = request.POST.get('id', '')
    department = request.POST.get('department', '')
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(department=department)
    return HttpResponse('saved')


def updatePhone(request):
    faculty_id = request.POST.get('id', '')
    phone = request.POST.get('phone', '')
    faculty = Faculty.objects.filter(faculty_name=faculty_id).update(
        phone=PhoneNumber.from_string(phone_number=phone, region='IN').as_e164)
    return HttpResponse('saved')


def updateEmail(request):
    faculty_id = request.POST.get('id', '')
    email = request.POST.get('email', '')
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(email=email)
    return HttpResponse('saved')


def updateWebsite(request):
    faculty_id = request.POST.get('id', '')
    website = request.POST.get('website', '')
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(website=website)
    return HttpResponse('saved')

def updateOffice(request):
    faculty_id = request.POST.get('id', '')
    office = request.POST.get('office', '')
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(office=office)
    return HttpResponse('saved')

def updateBiography(request):
    faculty_id = request.POST.get('id', '')
    biography = request.POST.get('biography', '')
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(biography=biography)
    return HttpResponse('saved')

def updateFacultyType(request):
    faculty_id = request.POST.get('id', '')
    faculty_type = request.POST.get('faculty_type', '')
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(faculty_type=faculty_type)
    return HttpResponse('saved')

def updateSpecializations(request):
    faculty_id = request.POST.get('id', '')
    specializations = request.POST.get('specializations', '')
    arr = []
    for specialization in specializations:
        t = Topic()
        t.topic_name = specialization
        arr.append(t)
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(specializations=arr)
    return HttpResponse('saved')

def updateQualifications(request):
    faculty_id = request.POST.get('id', '')
    qualifications = request.POST.get('qualification', '')
    arr = []
    for qualification in qualifications:
        q = Qualification()
        q.degree = qualification[0]
        q.institute = qualification[1]
        q.from_year = qualification[2]
        q.to_year = qualification[3]
        q.field = qualification[4]
        arr.append(q)
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(qualifications=arr)
    return HttpResponse('saved')

def updateInterests(request):
    faculty_id = request.POST.get('id', '')
    interests = request.POST.get('interests', '')
    arr = []
    for interest in interests:
        t = Topic()
        t.topic_name = interest
        arr.append(t)
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(teaching_interests=arr)
    return HttpResponse('saved')

def updatePublications(request):
    faculty_id = request.POST.get('id', '')
    publications = request.POST.get('publications', '')
    arr = []
    for publication in publications:
        p = Publication()
        p.title = publication[0]
        p.description = publication[1]
        p.publisher = publication[2]
        p.publication_date = publication[3]
        p.publication_url = publication[4]
        arr.append(p)
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(qualifications=arr)
    return HttpResponse('saved')

def updateAccomplishments(request):
    faculty_id = request.POST.get('id', '')
    accomplishments = request.POST.get('accomplishments', '')
    arr = []
    for accomplishment in accomplishments:
        t = Topic()
        t.topic_name = accomplishment
        arr.append(t)
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(accomplishments=arr)
    return HttpResponse('saved')

def updateAwards(request):
    faculty_id = request.POST.get('id', '')
    awards = request.POST.get('awards', '')
    arr = []
    for award in awards:
        a = Award()
        a.title = award[0]
        a.description = award[1]
        a.issuer = award[2]
        a.issue_date = award[3]
        a.award_url = award[4]
        arr.append(a)
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(awards=arr)
    return HttpResponse('saved')

def updateOrganizations(request):
    faculty_id = request.POST.get('id', '')
    organizations = request.POST.get('organizations', '')
    arr = []
    for organization in organizations:
        o = Organization()
        o.organization_name = organization[0]
        o.position = organization[1]
        o.description = organization[2]
        o.emp_type = organization[3]
        o.location = organization[4]
        o.from_date = organization[5]
        o.to_date = organization[6]
        o.is_currently_working = organization[7]
        arr.append(o)
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(organizations=arr)
    return HttpResponse('saved')

def updateSubjects(request):
    faculty_id = request.POST.get('id', '')
    subjects = request.POST.get('subjects', '')
    arr = []
    for subject in subjects:
        t = Topic()
        t.topic_name = subject
        arr.append(t)
    faculty = Faculty.objects.filter(
        faculty_name=faculty_id).update(subjects=arr)
    return HttpResponse('saved')