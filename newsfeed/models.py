from django.db import models
from django.forms import ModelForm;
import datetime
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

class Questiondtl(models.Model):
	ques_title		=	models.CharField(max_length=1000)
	ques_content	=	models.TextField(blank=True,default='')
	ques_author		=	models.CharField(max_length=200,default='') #userid to be stored
	ques_createdt	=	models.DateTimeField('created date',default=datetime.datetime.now())
	ques_moddt		=	models.DateTimeField('modified date',default=datetime.datetime.now())
	ques_sponsored	=	models.CharField(max_length=1,default='N')#flag value to be Y or N
	ques_category	=	models.CharField(max_length=200,default='')
	ques_total_votes=	models.IntegerField(default=0)
	ques_slug		=	models.SlugField(unique=True)

	def __str__(self):
		return str(self.id) + '--'+str(self.ques_title)

class Optionsdtl(models.Model):
	question		=	models.ForeignKey(Questiondtl,on_delete=models.CASCADE)
	option_txt		=	models.TextField()
	option_createdt	=	models.DateTimeField('created date',default=datetime.datetime.now())
	option_moddt	=	models.DateTimeField('modified date',default=datetime.datetime.now())
	option_votes	=	models.IntegerField(default=0)
	option_perc		=	models.IntegerField(default=1)

	def __str__(self):
		return str(self.question.ques_title)+ ' -- ' + str(self.option_txt)



def pre_ques_save_reciever(sender,instance,*args,**kwargs):
	slug = slugify(instance.ques_title)

	exists = Questiondtl.objects.filter(ques_slug=slug).exists()

	if exists:
		slug = "%s-%s"%(slug,instance.id)

	instance.ques_slug = slug




pre_save.connect(pre_ques_save_reciever,sender=Questiondtl)
