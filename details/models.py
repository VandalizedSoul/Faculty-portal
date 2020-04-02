from djongo import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Qualification(models.Model):
    degree = models.CharField(max_length=30)
    institute = models.CharField(max_length=100)
    year = models.IntegerField(max_length=30)

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
    award_url = models.URLField(null=True, max_length=200)

    class Meta:
        abstract = True


class Organization(models.Model):
    organization_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    discription = models.TextField()
    duration = models.IntegerField(max_length=3)

    class Meta:
        abstract = True


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=30,null=True)
    designation = models.CharField(max_length=30,null=True)
    department = models.CharField(max_length=30,null=True)
    image = models.FileField(upload_to='', blank=True)
    qualifications = models.ArrayField(model_container=Qualification,null=True)
    phone = PhoneNumberField(blank=False, null=False,)
    # phone = models.CharField(max_length=30,null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(max_length=200,null=True)
    # address =
    office = models.CharField(max_length=30,null=True)
    biography = models.TextField(null=True)
    specializations = models.ArrayField(model_container=Topic,null=True)
    teaching_interests = models.ArrayField(model_container=Topic,null=True)
    accomplishments = models.ArrayField(model_container=Topic,null=True)
    publications = models.ArrayField(model_container=Publication,null=True)
    awards = models.ArrayField(model_container=Award,null=True)
    organizations = models.ArrayField(model_container=Organization,null=True)
    faculty_type = models.CharField(max_length=10,null=True)
