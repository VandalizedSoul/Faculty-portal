from djongo import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))

DEPT_LIST =[('CE','CE'), ('IT','IT'), ('IC','IC'), ('CL','CL'), ('EC','EC'), ('CH','CH'), ('MH','MH')]


class Certification(models.Model):
    credential_title = models.CharField(max_length=30)
    credential_id = models.CharField(max_length=100)
    credential_url = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    issuing_organization = models.CharField(max_length=100)


class Qualification(models.Model):
    degree = models.CharField(max_length=30)
    institute = models.CharField(max_length=100)
    from_year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    to_year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    field = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Topic(models.Model):
    topic_name = models.CharField(max_length=50, null=True)

    class Meta:
        abstract = True


class Publication(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    publisher = models.CharField(max_length=30)
    publication_date = models.DateField()
    publication_url = models.URLField(max_length=200)

    class Meta:
        abstract = True


class Award(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    issuer = models.CharField(max_length=30)
    issue_date = models.DateField()
    award_url = models.URLField(max_length=200)
    class Meta:
        abstract = True


class Organization(models.Model):
    organization_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    description = models.TextField()
    emp_type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    from_date = models.DateField()
    to_date = models.DateField()
    is_currently_working = models.BooleanField()

    class Meta:
        abstract = True


class Faculty(models.Model):
    faculty_id = models.CharField(max_length=7, null=True)
    faculty_name = models.CharField(max_length=30, null=True)
    designation = models.CharField(max_length=30, null=True)
    department = models.CharField(max_length=2, choices=DEPT_LIST, null=False, default='CE')
    image = models.ImageField(upload_to='', blank=True)
    qualifications = models.ArrayField(model_container=Qualification, null=True)
    phone = PhoneNumberField(blank=False, null=False,)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(max_length=200, null=True)
    office = models.CharField(max_length=30, null=True)
    biography = models.TextField(null=True)
    specializations = models.ArrayField(model_container=Topic, null=True)
    teaching_interests = models.ArrayField(model_container=Topic, null=True)
    accomplishments = models.ArrayField(model_container=Topic, null=True)
    publications = models.ArrayField(model_container=Publication, null=True)
    awards = models.ArrayField(model_container=Award, null=True)
    organizations = models.ArrayField(model_container=Organization, null=True)
    faculty_type = models.CharField(max_length=10, null=True)
    subjects = models.ArrayField(model_container=Topic, null=True)

    class Meta:
        verbose_name_plural = "faculties"
  

class Access(models.Model):
    faculty_id = models.BooleanField() 
    faculty_name = models.BooleanField() 
    designation = models.BooleanField() 
    department = models.BooleanField() 
    image = models.BooleanField() 
    qualifications = models.BooleanField() 
    phone = models.BooleanField() 
    email = models.BooleanField() 
    website = models.BooleanField() 
    office = models.BooleanField() 
    biography = models.BooleanField() 
    specializations = models.BooleanField() 
    teaching_interests = models.BooleanField() 
    publications = models.BooleanField() 
    awards = models.BooleanField() 
    organizations = models.BooleanField() 
    faculty_type = models.BooleanField() 