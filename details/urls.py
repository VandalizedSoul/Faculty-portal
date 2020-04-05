from django.urls import path

from . import views
from django.conf.urls import url
from . import views
from details.views import login, auth_view, home,facultydetails, invalidlogin



urlpatterns = [
    path('', views.index, name='index'),
    # url(r'Home', views.HomePageView.as_view()),
    url(r'^login/$', login),
    url(r'^addinfo/$', views.addinfo),
    url(r'^auth/$', auth_view),
    url(r'^home/$', home),
    url(r'^facultydetails/$', facultydetails),
    url(r'^invalidlogin/$', invalidlogin),
]