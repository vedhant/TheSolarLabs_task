from django import forms
from . import models

class CreateDemoUser(forms.ModelForm):
	class Meta:
		model = models.UserDemo
		fields = ['name', 'phone', 'email']