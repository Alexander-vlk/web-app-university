from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


from .models import UserDataModel


class UserDataForm(forms.ModelForm):
	class Meta:
		model = UserDataModel
		fields = ['fio', 'phone', 'email', 'gender', 'birth', 'user_langs', 'biography']


class AuthUserForm(forms.ModelForm, AuthenticationForm):
	class Meta:
		model = User
		fields = ('username', 'password')

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

