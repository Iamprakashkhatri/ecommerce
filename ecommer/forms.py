from django import forms
from .models import Member

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # email=forms.CharField(widget=forms.EmailField())

    class Meta:
        model = Member
        fields = ['email','password']