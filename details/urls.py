from django.urls import path

from . import views
from django.conf.urls import url
from . import views
from details.views import home, facultydetails, invalidlogin, profile_image_view, success
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
# login, auth_view,


urlpatterns = [
    path('', views.index, name='index'),
    # url(r'Home', views.HomePageView.as_view()),
    # url(r'^login/$', login),
    url(r'^addinfo/$', views.addinfo),
    # url(r'^auth/$', auth_view),
    url(r'^home/$', home),
    url(r'^facultydetails/(?P<faculty_id>[a-zA-Z0-9]+)/$', views.facultydetails, name='facultydetails'),
    url(r'^invalidlogin/$', invalidlogin),
    path('create/', views.QualificationCreateView.as_view(), name='create_qualification'),
    path('update/<int:pk>', views.QualificationUpdateView.as_view(), name='update_qualification'),
    path('read/<int:pk>', views.QualificationReadView.as_view(), name='read_qualification'),
    path('delete/<int:pk>', views.QualificationDeleteView.as_view(), name='delete_qualification'),
    path('image_upload', profile_image_view, name='image_upload'),
    path('success', success, name='success'),
    url(r'^updateImage/(?P<faculty_id>[a-zA-Z0-9]+)/$', updateImage, name="updateImage"),
    # path('signup/', views.SignUpView.as_view(), name='signup'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)