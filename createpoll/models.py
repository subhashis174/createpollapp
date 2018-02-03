from django.db import models
from django import forms
from django.forms import ModelForm, Textarea,TextInput
from newsfeed.models import Optionsdtl,Questiondtl
# Create your models here.


class QuestionForm(forms.ModelForm):
	class Meta:
		model = Questiondtl
		fields = ('ques_title',)
		widgets = {
			'ques_title' : TextInput(attrs={'class':'form-control crpollinp','id':'ques','placeholder':'Enter Question title here...'}),
		}
		labels = {
			'ques_title' : ''
		}
	

class OptionForm(forms.ModelForm):
	class Meta:
		model = Optionsdtl
		fields = ('option_txt',)
		widgets = {
			'option_txt' : Textarea(attrs={'class':'form-control crpollinp','placeholder':'Enter Option details here...','rows':1}),
		}
		labels = {
			'option_txt' : ''
		}
