from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from .models import QuestionForm,OptionForm
from newsfeed.models import Optionsdtl,Questiondtl
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
# Create your views here.

def createpolls(request):
	#this method does nothing.just for practising sake
	form = PollForm()
	
	
	
	tmp			=	get_template('createpoll.html')
	html 		=	tmp.render(
					dict({		#changed to dict from Context on migrating from django1.10 to django2.0
						'form':form,
						'user' : user,
						'email':useremail,
						'us':request.session[str(useremail)]
						})
					)
	return HttpResponse(html)

def create(request):
	if request.method == "GET":
		try:
			print("hello ji")
			user = request.user
			useremail = User.objects.get(username=user.username).email
			print("\n")
			print("Create Page-GET method")
			print(useremail)
			print("\n")
		except User.DoesNotExist:
			login_flag = False


		form1 = QuestionForm();
		form2 = OptionForm(prefix='1');
		form3 = OptionForm(prefix='2');
		form4 = OptionForm(prefix='3');
		form5 = OptionForm(prefix='4');
		return render(request,'createpoll.html',{'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'email':useremail});
	elif request.method == "POST":
		try:
			print("hello ji")
			user = request.user
			useremail = User.objects.get(username=user.username).email
			print("\n")
			print("Create Page-POST method")
			print(useremail)
			print("\n")
		except User.DoesNotExist:
			login_flag = False

		form1 = QuestionForm(request.POST);
		form1.save();
		print("\n")
		print(Questiondtl.objects.get(ques_title=request.POST['ques_title']).id)
		print("\n")
		form1 = Questiondtl.objects.get(ques_title=request.POST['ques_title'])
		form1.ques_author= useremail #User.objects.get(username=request.user.username).email
		#form1.ques_createdt = datetime.datetime.now();
		#form1.ques_moddt = datetime.datetime.now();
		form1.ques_sponsored = 'N';
		form1.ques_category = 'Misc';
		form1.save();

		#check for questions created for the ques_title and the logged in
		obj = Questiondtl.objects.get(ques_title=request.POST['ques_title'])

		
		obj1 = Optionsdtl();
		obj1.question = obj;
		obj1.option_txt = request.POST['1-option_txt'];
		obj2 = Optionsdtl();
		obj2.question = obj;
		obj2.option_txt = request.POST['2-option_txt'];
		obj3 = Optionsdtl();
		obj3.question = obj;
		obj3.option_txt = request.POST['3-option_txt'];
		obj4 = Optionsdtl();
		obj4.question = obj;
		obj4.option_txt = request.POST['4-option_txt'];
		
		form1.save();
		obj1.save();
		obj2.save();
		obj3.save();
		obj4.save();
		#form2.save();
		return HttpResponseRedirect('/');

