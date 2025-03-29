from .models import Image
from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ( 'title', 'photo','user')


class LoginForm(forms.Form):
    user_email = forms.EmailField(max_length=100)
    password   = forms.CharField(max_length=100)

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [ 'username', 'password1', 'password2']