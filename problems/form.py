from django import forms
from django.forms import ModelForm
from .models import Submissions



#submission form
class SubmissionForm(forms.ModelForm):
    #name=forms.CharField(label='nameofProblem',initial='')
    
    codefile=forms.FileField(label='Your file')
    #lang_used=forms.ChoiceField(label='Language',widget=forms.Select(),choices = ([('java','java'), ('c','c'),('cpp','cpp'), ]), initial='java', required = True,))
    lang_used = forms.ChoiceField(widget = forms.Select(), 
                     choices = ([('java','java'), ('cpp','cpp'),('c','c'),('python','python'),]), initial='java', required = True,)

    
    class Meta:
        model=Submissions
        exclude=('Code','name','developer')

