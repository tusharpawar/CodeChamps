from django.contrib import admin
from .models import problem
from .models import Submissions

# Register your models here.
class problemAdmin(admin.ModelAdmin):
    list_display=['id','title','added_on']

    class Meta:
        model=problem


admin.site.register(problem,problemAdmin)
admin.site.register(Submissions)
