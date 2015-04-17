from django.db import models
from problems.files import get_path
from Developers.models import Developer


# Create your models here.
class problem(models.Model):
    title=models.CharField(max_length=400,unique=True)
    body=models.TextField()
    added_on=models.DateField(auto_now_add=True,auto_now=False)
    
    input_format=models.TextField()
    output_format=models.TextField()
    ip_tc=models.FileField(upload_to='input/',null=True,blank=True)
    op_tc=models.FileField(upload_to='output/',null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Problem"
        verbose_name_plural="Problems"
        ordering=["-id"]
    
def _upload_path(instance,filename):
    return instance.get_upload_path(filename)

class Submissions(models.Model):
    name=models.CharField(max_length=200)
    #developer=models.ForeignKey(Developer)
    Code=models.FileField(upload_to=_upload_path,null=True,blank=True)
##    lang_used_choices=(
##        ('java','java'),  
##        ('c','c'),
##        ('cpp','cpp'),
##        ('python','python'),
##        )
##    lang_used=models.CharField(choices=lang_used_choices,max_length=10)

    def get_upload_path(self,filename):
        return "submissions/"+self.name+"/"+filename

    def __str__(self):
        return self.Code


class Solved(models.Model):
    username=models.CharField(max_length=200)
    problemname=models.CharField(max_length=200)
    marks=models.IntegerField(default=0)

    def __str__(self):
        return self.problemname


