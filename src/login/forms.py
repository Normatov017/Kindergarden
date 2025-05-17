from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Foydalanuvchi nomi')
    password = forms.CharField(widget=forms.PasswordInput, label='Parol')

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Parol')

    class Meta:
        model = User
        fields = ['username', 'full_name', 'password']
