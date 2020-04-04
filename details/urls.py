from django.urls import path
from details.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('addFaculty', addFaculty),
    path('show', getAllFaculty),
    path('', index, name='index'),
]