import random, string
from django.contrib.contenttypes.models import ContentType
from Developers.models import Developer

 
##def get_path(instance,request):
##    #ctype = ContentType.objects.get_for_model(instance)
##    ctype=ContentType.objects.get_for_model(Developer)
##    model = ctype.model
##    app = ctype.app_label
##    #extension = filename.split('.')[-1]
##   # dir = "site"
####    if request.user.is_authenticated():
####        dev=Developer.objects.get(user=request.user)
####    if model == "job":
####        dir += "/pdf/job_attachment"
####    else:
##    dir = "/submissions/%s" % app
####        if model == "image_type_1":
####            dir += "/type1/%s" % instance.category
####        elif model == "image_type_2":
####            dir += "/type2"
####        elif model == "restaurant":
####            dir += "/logo"
####        else:
####            dir += "/%s" % model
####    
##    chars = string.letters + string.digits
##    name = string.join(random.sample(chars, 8), '')
##    
##    return "%s/" % (dir)
def get_path(instance,filename):
    #if request.user.is_authenticated();
    #dev=Developer.objects.get(user=request.user)
    ctype=ContentType.objects.get_for_model(instance)
    model=ctype.model
    developer=ctype.developer
    dir="submissions/%s" % developer.user.username
    print dir
    return dir
