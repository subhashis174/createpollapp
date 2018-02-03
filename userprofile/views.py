from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.template import Template,Context
from django.template.loader import get_template

# Create your views here.

def userprofile(request,username):
	tmp			=	get_template('userprofile.html')
	html 		=	tmp.render(
					dict({		#changed to dict from Context on migrating from django1.10 to django2.0
						'username' : username
						})
					)
	return HttpResponse(html)

