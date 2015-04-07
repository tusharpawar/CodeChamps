from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import RegistrationForm,LoginForm,UpdateForm,ChangePasswordForm,ProfilePicUploadForm
from django.template import RequestContext
from django.contrib.auth.models import User
from .models import Developer
from django.contrib.auth import authenticate,login,logout
import uuid

#gives a unique ref to user
def get_refid():
    ref_id=str(uuid.uuid4())[:11].replace('-','').lower()
    try:
        obj=Developers.objects.get(ref_id=ref_id)
        get_refid()
    except:
        return ref_id

#view for user registraion
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
                                          password=form.cleaned_data['password'],
                                         )
            s=get_refid()
            #print s
            user.save()
            developer=Developer(user=user,name=form.cleaned_data['name'],ref_id=s,                                                         #propic=form.cleaned_data['propic'],
                      country=form.cleaned_data['country'])
            developer.save()
            return HttpResponseRedirect('/profile/'+s)
             
        else:
            return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
    else:
        #show blank form
        form=RegistrationForm
        context={'form':form}
        return render_to_response('register.html',context,context_instance=RequestContext(request))

#view for login
def LoginRequest(request):
    if request.user.is_authenticated():
        dev=Developer.objects.get(user=request.user)
        red_link='/profile/'+dev.ref_id
        return HttpResponseRedirect(red_link)
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

#User logout view
def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')

#user profile view
def Profile(request,ref_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    
    developer=Developer.objects.get(ref_id=ref_id)    
    #print ref_id,developer
    developer1=Developer.objects.get(user=request.user)
    allowEdit=False
    if(ref_id==developer1.ref_id):
        allowEdit=True
        
    context={'developer':developer,'Edit':allowEdit}              
    return render_to_response('profile.html',context,context_instance=RequestContext(request))

#user profile update view
def UpdateProfile(request,ref_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    form=UpdateForm(request.POST)
    developer=Developer.objects.get(ref_id=ref_id)
    if request.method=='POST':
        success=False
        if form.is_valid():
            developer.name=form.cleaned_data['name']
            developer.user.email=form.cleaned_data['email']
            developer.save()
            success=True
            context={'developer':developer,'update':success,'edit':True}
            red_link='/profile/'+developer.ref_id
            return HttpResponseRedirect(red_link)
        else:
            Error='Invalid inputs'
            return render_to_response('updateprofile.html',{'form':form,'developer':developer,'error':Error},context_instance=RequestContext(request)) 
    else:
        return render_to_response('updateprofile.html',{'form':form,'developer':developer},context_instance=RequestContext(request))
    
    
#user password change view

def ChangePassword(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    form=ChangePasswordForm(request.POST)
    #user=request.user
    developer=Developer.objects.get(user=request.user)
    if request.method=='POST':
        if form.is_valid():
            original=form.cleaned_data['original']
            if(request.user.check_password(original)):
                password=form.cleaned_data['new_password']
                password1=form.cleaned_data['new_password_verify']
                if(password==password1):
                    request.user.set_password(password)
                    request.user.save()
                    username=request.user.username
                    logout(request)
                    user=authenticate(username=username,password=password)
                    if(user is not None):
                        login(request,user)
                        red_link='/profile/'+developer.ref_id
                        return HttpResponseRedirect(red_link)
                else:
                    Error="New Passwords do not match"
                    return render_to_response('changepassword.html',    {'form':form,'developer':developer,'error':Error},context_instance=RequestContext(request)) 
            else:
                Error="Original Password is not matching"
                return render_to_response('changepassword.html',        {'form':form,'developer':developer,'error':Error},context_instance=RequestContext(request)) 
        else:
            return render_to_response('changepassword.html',{'form':form,'developer':developer},context_instance=RequestContext(request)) 
    else:
        return render_to_response('changepassword.html',{'form':form,'developer':developer},context_instance=RequestContext(request)) 

                
        
#change profile pic
def upload_profile_pic(request):
    form = ProfilePicUploadForm(request.POST, request.FILES) 
    dev = Developer.objects.get(user=request.user)
    print 1
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    print 2
    if request.method == 'POST':
        print 3
        print form.is_valid(),form.errors 
        if form.is_valid():
            dev = Developer.objects.get(user=request.user)
            dev.propic.delete(False)
            dev.propic = request.FILES['image']
            print dev.propic,request.FILES['image']
            dev.save()
            return render_to_response('profile.html',{'Message':'Success ic changeing pic'} ,context_instance=RequestContext(request)) 
           
        else:
                Error="image invlaid"
                return render_to_response('changeprofilepic.html',          {'form':form,'developer':dev,'error':Error},context_instance=RequestContext(request)) 
    else:
                return render_to_response('changeprofilepic.html',  {'form':form,'developer':dev},context_instance=RequestContext(request)) 
    
    #    return render_to_response('changeprofilepic.html',{'form':form,'developer':dev},context_instance=RequestContext(request)) 
        
        