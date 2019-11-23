from django import forms

from .models import *


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = '__all__'

