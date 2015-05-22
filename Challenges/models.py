from django.db import models
from problems.models import problem
from Developers.models import Developer
# Create your models here.
class Challenge(models.Model):
    challenge_name=models.CharField(max_length=200,unique=True)
    challenge_body=models.TextField()
    challenge_rules=models.TextField()
    added_on=models.DateField(auto_now_add=True,auto_now=False)
    problemlist=models.ManyToManyField(problem )
    start_time = models.DateTimeField("Event start Time",blank=True,null=True)
    end_time = models.DateTimeField("Event End Time",blank=True,null=True)
    dp=models.ImageField(upload_to='competitions/')
    participents=models.ManyToManyField(Developer,blank=True,null=True)
    def __str__(self):
        return self.challenge_name

    class Meta:
        verbose_name="Challenge"
        verbose_name_plural="Challenges"
        ordering=["-id"]
    
