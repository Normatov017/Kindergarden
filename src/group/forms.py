from django import forms
from .models import Group, Kid

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']  # yoki sizda bo'lgan boshqa fieldlar


class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['full_name', 'age', 'group', 'status']
