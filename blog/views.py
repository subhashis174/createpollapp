from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from blog.models import BlogArticle

# Create your views here.

def blogpage(request):
	#Blogs	=	BlogArticle.objects.all()
	#tmp			=	get_template('blogs.html')
	#html 		=	tmp.render(
	#				Context({
	#					'blogs':Blogs
	#					})
	#				)
	html = "<h1>Blogs</h1>"
	return HttpResponse(html)
