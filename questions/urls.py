#from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin

from . import views
app_name	=	'questions'
urlpatterns = [
	url('',views.create,name='questions'),
]