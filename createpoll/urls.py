#from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin

from . import views
app_name	=	'createpoll'
urlpatterns = [
	url('',views.create,name='createpolls'),
]