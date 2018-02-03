from django.db import models
from django.forms import ModelForm;
import datetime


# Create your models here.
class UserInfo(models.Model):
	Username	=	models.CharField(max_length=100,default='')
	Fname		=	models.CharField(max_length=100,default='')
	Mname		=	models.CharField(max_length=100,blank=True,default='')
	Lname		=	models.CharField(max_length=100,blank=True,default='')
	Age			=	models.IntegerField(default=0)
	Sex			=	models.CharField(max_length=25,blank=True,default='')
	Emailid		=	models.EmailField(null=True)
	Password	=	models.CharField(max_length=100,blank=True,default='')
	createdt	=	models.DateTimeField(default=datetime.datetime.now())
	modifieddt	=	models.DateTimeField(default=datetime.datetime.now())
	lastlogindt	=	models.DateTimeField(default=datetime.datetime.now())
	fblogin		=	models.CharField(max_length=10,blank=True,default='N')
	gpluslogin	=	models.CharField(max_length=10,blank=True,default='N')
	userimg		=	models.ImageField(blank=True,default='')


	def __str__(self):
		return str(self.id) + '--' + str(self.Username)