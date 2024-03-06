from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserRegistrationForm(UserCreationForm):
    firstname=forms.CharField(max_length=101)
    lastname=forms.CharField(max_length=101)
    email=forms.EmailField()
    phone=forms.IntegerField()
    class Meta:
        model=User
        fields=['username','firstname','lastname','email','phone','password1','password2']