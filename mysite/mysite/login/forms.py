from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #Take out help messages
        help_texts = {k:"" for k in fields}

class UserEditForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    descripcion =  forms.CharField(max_length=50)
    web_link = forms.URLField(max_length=200)
    class Meta:
      model = Usuario
      fields = ['email', 'first_name', 'last_name', 'descripcion', 'web_link', 'descripcion']
      #Take out help messages
      help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
  image = forms.ImageField()
  class Meta:
      model = User
      fields = ['image']