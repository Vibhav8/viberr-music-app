from django.contrib.auth.models import User #to import the generic view of user model from admin
from django import forms
from .models import Album,Song

class UserForm(forms.ModelForm): #blueprint of user form
	password = forms.CharField(widget=forms.PasswordInput) #password is not in admin user by default hence we have to declare it..widget=forms.PasswordInput = this to to make *** when inputting password
	class Meta: #information about class
		model = User # user model from admin
		fields = ['username','email','password']

class SongForm(forms.ModelForm):

	class Meta:
		model = Song
		fields = ['song_title','audio_file']
