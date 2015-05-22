from django.contrib import admin
from .models import Challenge

# Register your models here.
##class ChallengeAdmin(admin.ModelAdmin):
##    list_display['id','challenge_name','problemlist']

    
admin.site.register(Challenge)
