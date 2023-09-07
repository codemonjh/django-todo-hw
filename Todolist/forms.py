from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Todolist.models import Todolist


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]


class TodolistForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['subject', 'content', 'is_complete']
