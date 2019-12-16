from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm

from django import forms

class UserCreateForm(UserCreationForm):
    email = forms.CharField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username", "email","image", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.image = self.cleaned_data["image"]
        if commit:
            user.save()
        return user


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','image']