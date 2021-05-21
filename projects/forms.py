from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, models

from .models import Project


class PostForm(ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
