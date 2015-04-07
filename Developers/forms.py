from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Developer

#Registraion Form
class RegistrationForm(ModelForm):
    username=forms.CharField(label='User name')
    email=forms.EmailField(label='Email')
    password=forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False))
    password1=forms.CharField(label='Verify Password',widget=forms.PasswordInput(render_value=False))

    class Meta:
        model=Developer
        exclude=('user','problems_list','ref_id','prpoic')
    #CHEKING VALID USERNAME
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
    
    
    
#Login Form
class LoginForm(forms.Form):
    username=forms.CharField(label='User name')
    password=forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False))

#Profile Update Form
class UpdateForm(forms.Form):
    name=forms.CharField(label='Name')
    email=forms.EmailField(label='Email')
    
# Password Change

class ChangePasswordForm(forms.Form):
    original=forms.CharField(label='Original',widget=forms.PasswordInput(render_value=False))
    new_password=forms.CharField(label='New Password',widget=forms.PasswordInput(render_value=False))
    new_password_verify=forms.CharField(label='Verify New Password',widget=forms.PasswordInput(render_value=False))

#profile pic upload form
class ProfilePicUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField(label='Your new image' )
   