from django import forms
from django.db.models import fields
from .models import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        labels=('password1','Password','password2','Confirm_Password')

class ProfileForm(forms.ModelForm):
    address=forms.Textarea()
    class Meta:
        model=Register
        fields=('address','phone_number')