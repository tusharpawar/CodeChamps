from django.shortcuts import render
from .models import Challenge
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from Developers.models import Developer
import datetime
from django.utils import timezone
# Create your views here.

def AllChallenges(request):
    if request.user.is_authenticated():
        dev=Developer.objects.get(user=request.user)
    else :
        dev=None
    challenges=Challenge.objects.all().order_by('id')
    context={'challenges':challenges,'developer':dev}
    return render_to_response('challenges.html',context,context_instance=RequestContext(request));


def register_for_challenge(request,challenge_name):
    if request.user.is_authenticated():
        dev=Developer.objects.get(user=request.user)
    else:
        dev=None
    
    challenge=Challenge.objects.get(challenge_name=challenge_name)
    challenge.participents.add(dev)
    challenge.save()
    red_link='/challenges/'+challenge_name
    return HttpResponseRedirect(red_link)

def SpecificChallenge(request,challenge_name):
    if request.user.is_authenticated():
        developer=Developer.objects.get(user=request.user)
    else:
        developer=None
    challenge=Challenge.objects.get(challenge_name=challenge_name)
    cnt=challenge.participents.count()
    try:
        dev=challenge.participents.get(name=developer.name)
    except:
        dev=None
    problemlist=challenge.problemlist.all()
    now = timezone.now()
    start=challenge.start_time
    end=challenge.end_time
    msg=''
    print "devloper"
    print dev,dev==None and now<end
    if dev==None and now<end:
        print 1
        msg="Register"
    else: 
        print 2
        if dev:
            if now>start:
                msg="Allow"
            if now>end:
                msg="Ended"
            if now<start:
                msg="Participated"
    
    context={'challenge':challenge,'problemlist':problemlist,'developer':developer,'now':now,'start':start,'msg':msg,'cnt':cnt}
    challenge.challenge_body="<br>".join(challenge.challenge_body.split("\n"))
    challenge.challenge_rules="<br>".join(challenge.challenge_rules.split("\n"))
    return render_to_response('specificchallenge.html',context,context_instance=RequestContext(request));
