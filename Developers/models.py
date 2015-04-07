from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Developer(models.Model):
        user=models.OneToOneField(User)
        name=models.CharField(max_length=200)
        propic=models.ImageField(upload_to="profilepics/",null=True,blank=True)
        country=models.CharField(max_length=100,default="INDIA")
        ref_id=models.CharField(max_length=100,default="ABC",null=True)
        problems_list=models.CharField(max_length=1000,null=True)
        joined_on=models.DateField(auto_now_add=True,auto_now=False)

        def __str__(self):
            return self.name

