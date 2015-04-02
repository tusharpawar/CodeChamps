from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import RegistrationForm,LoginForm
from django.template import RequestContext
from django.contrib.auth.models import User
from .models import Developer
from django.contrib.auth import authenticate,login,logout
import uuid
# Create your views here.

def get_refid():
    ref_id=str(uuid.uuid4())[:11].replace('-','').lower()
    try:
        obj=Developers.objects.get(ref_id=ref_id)
        get_refid()
    except:
        return ref_id
def DeveloperRegistrations(request):
    
    if request.user.is_authenticated():
        dev=Developer.objects.get(user=request.user)
        red_link='/profile/'+dev.ref_id
        return HttpResponseRedirect(red_link)
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(username=form.cleaned_data['username'],
                                          email=form.cleaned_data['email'],
                                          password=form.cleaned_data['password'])
            s=get_refid()
            print s
            user.save()
            developer=Developer(user=user,name=form.cleaned_data['name'],ref_id=s)
            developer.save()
            return HttpResponseRedirect('/profile/'+s)
             
        else:
            return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
    else:
        #show blank form
        form=RegistrationForm
        context={'form':form}
        return render_to_response('register.html',context,context_instance=RequestContext(request))

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')

    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            developer=authenticate(username=username,password=password)
            if developer is not None:
                login(request,developer)
                dev=Developer.objects.get(user=developer)
                red_link='/profile/'+dev.ref_id
                return HttpResponseRedirect(red_link)
            else:
                return render_to_response('index.html',{'form':form,'message':"Invalid credentials"},context_instance=RequestContext(request))        
        else:
             return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))        
            
    else:
        #show blank form
        form=LoginForm
        context={'loginform':form}
        return render_to_response('index.html',context,context_instance=RequestContext(request))

def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')

def Profile(request,ref_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    
    developer=Developer.objects.get(ref_id=ref_id)    
    print ref_id,developer
    developer1=Developer.objects.get(user=request.user)
    allowEdit=False
    if(ref_id==developer1.ref_id):
        allowEdit=True
        
    context={'developer':developer,'Edit':allowEdit}              
    return render_to_response('profile.html',context,context_instance=RequestContext(request))
    