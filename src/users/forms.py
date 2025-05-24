
from django import forms
from .models import User


class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'role', 'is_active']
