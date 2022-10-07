from django import forms
from app1.models import Register
class RegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=3)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=3)
    class Meta():
        model=Register
        fields='__all__'

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=3)

    class Meta():
        model=Register
        fields=('Email','Password')  

class UpdateForm(forms.ModelForm):
    class Meta():
        model=Register
        fields=('Email','Name','Age','Place')
