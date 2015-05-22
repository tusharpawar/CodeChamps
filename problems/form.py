from django import forms
from django.forms import ModelForm
from .models import Submissions



#submission form
class SubmissionForm(forms.ModelForm):
    codefile=forms.FileField(label='Your file')
    lang_used = forms.ChoiceField(widget = forms.Select(), 
                     choices = ([('java','java'), ('cpp','cpp'),('c','c'),('python','python'),]), initial='java', required = True,)

    
    class Meta:
        model=Submissions
        exclude=('Code','name','developer')

