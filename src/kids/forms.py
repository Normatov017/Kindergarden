from django import forms
from .models import Kid

class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['full_name', 'age', 'group', 'status']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "To‘liq ismi"}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Yosh"}),
            'group': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }



class KidCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['full_name', 'age', 'group', 'status']
        labels = {
            'full_name': 'Ism Familiya',
            'age': 'Yosh',
            'group': 'Guruh',
            'status': 'Holati',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism va familiya kiriting'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Yoshni kiriting'
            }),
            'group': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(choices=[
                ('active', 'Faol'),
                ('inactive', 'Nofaol')
            ], attrs={
                'class': 'form-select'
            })
        }
