from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PostModel

class registerUserForm(UserCreationForm):
    
    class Meta:
        model = User

        fields = ('username',)

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel

        fields = [
            'title',
            'description'
        ]