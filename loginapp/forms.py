from django import forms
from .models import Profile

class ProfileInfoForm(forms.Form):
    username = forms.CharField(max_length=50);
    password = forms.CharField(widget=forms.PasswordInput);
    portfolio_url = forms.URLField();
    
