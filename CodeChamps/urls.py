from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
#from django.contrib.auth.views import
from django.conf.urls.static import static  
from django.conf import settings
from Developers import forms
from django.contrib.auth import views as auth_views
urlpatterns = patterns('',
    # url for developers
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    # url(r'^blog/', include('blog.urls')),
    (r'^$','Developers.views.LoginRequest'),   
    (r'^admin/', include(admin.site.urls)),
    (r'^register/$','Developers.views.DeveloperRegistrations'),
    (r'^login/$','Developers.views.LoginRequest'),
    (r'^logout/$','Developers.views.LogoutRequest'),
    (r'^profile/(?P<ref_id>.*)$','Developers.views.Profile'),
    (r'^updateprofile/(?P<ref_id>.*)$','Developers.views.UpdateProfile'),
    (r'^changepassword/$','Developers.views.ChangePassword'),
    (r'^changeprofilepic/$','Developers.views.upload_profile_pic'),
    (r'^changeprofilepic/removeprofilepic/$','Developers.views.remove_profile_pic'),
    (r'^reset/$','Developers.views.reset_password'),
    ###url for problems
    url(r'^problems/$','problems.views.AllProblems'),
    url(r'^problems/(?P<title>.*)/$','problems.views.SpecificProblem'),
    #url(r'^problems/file/$','problems.views.CreateFile'),
    url(r'^submissions/(?P<title>.*)$', 'problems.views.upload_submission'),
    #url(r'^submissions/*$','problems.views.display_file'),
    #url(r'^runbatch/$','problems.views.run_batch'),

     ##url for challenges
    url(r'^challenges/$','Challenges.views.AllChallenges'),
    url(r'^challenges/(?P<challenge_name>.*)/$','Challenges.views.SpecificChallenge'),
    url(r'^register/(?P<challenge_name>.*)/$','Challenges.views.register_for_challenge')


)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


