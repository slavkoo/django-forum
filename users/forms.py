from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

	username = forms.CharField(max_length=50, label='Ime')
	password1 = forms.CharField(max_length=50, label='Sifra', widget = forms.PasswordInput())
	password2 = forms.CharField(max_length=50, label='Potvrdi sifru', widget = forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']