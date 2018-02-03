#from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin

from . import views
app_name    =   'userprofile'
urlpatterns = [
    url(r'^profile/(?P<username>\d+)',views.userprofile,name='userprofile'),
]