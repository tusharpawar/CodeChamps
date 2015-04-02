from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Developer
'''#new
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.contrib.sites.models import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template import loader
import datetime
'''
class RegistrationForm(ModelForm):
    username=forms.CharField(label='User name')
    email=forms.EmailField(label='Email')
    password=forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False))
    password1=forms.CharField(label='Verify Password',widget=forms.PasswordInput(render_value=False))

    class Meta:
        model=Developer
        exclude=('user','problems_list','ref_id')

    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username not available select another')

    def clean(self):
        if 'password' in self.cleaned_data and 'password1' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The password does not match ")
        return self.cleaned_data
    
class LoginForm(forms.Form):
    username=forms.CharField(label='User name')
    password=forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False))

