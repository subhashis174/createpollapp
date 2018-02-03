from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from newsfeed.models import Questiondtl,Optionsdtl
from userprofile.models import UserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages  

# Create your views here.

def questionpage(request,question):
	Questdtl	=	Questiondtl.objects.filter(ques_slug=question)
	Optiondtl	=	Optionsdtl.objects.all()
	Userinfo	=	UserInfo.objects.all()
	
	Userinfo	=	UserInfo.objects.all()

	for ques in Questdtl:
		for opt in Optiondtl:
			if opt.question.id == ques.id:
				if ques.ques_total_votes == 0:
					opt.option_perc = (opt.option_votes)*100
				else:
					opt.option_perc = (opt.option_votes)*100/(ques.ques_total_votes)

	for ques in Questdtl:
		fname=User.objects.get(email=ques.ques_author).first_name
		lname=User.objects.get(email=ques.ques_author).last_name
		ques.ques_author = fname + ' ' + lname
		ques.ques_moddt = ques.ques_moddt.strftime('%d,%b %Y')

	try:
		user = request.user
		useremail = User.objects.get(username=user.username).email
		print("\n")
		print("Questions Page")
		print(useremail)
		login_flag=True
		print("\n")
	except User.DoesNotExist:
		login_flag = False

	print("\n")
	print(login_flag)
	print("\n")
	print(question)


	tmp			=	get_template('question.html')
	html 		=	tmp.render(
					dict({		#changed to dict from Context on migrating from django1.10 to django2.0
						'questiondtl':Questdtl,
						'optiondtl' : Optiondtl,
						'question' : question,
						'login_flag':login_flag
						})
					)
	return HttpResponse(html)