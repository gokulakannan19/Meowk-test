from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Post, Blogger


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['blogger']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BloggerForm(ModelForm):

    class Meta:
        model = Blogger
        fields = "__all__"
        exclude = ["user"]
