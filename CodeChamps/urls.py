from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
#from django.contrib.auth.views import
from django.conf.urls.static import static  
from django.conf import settings
from Developers import forms
from django.contrib.auth import views as auth_views
urlpatterns = patterns('',
    # Examples:
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
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


