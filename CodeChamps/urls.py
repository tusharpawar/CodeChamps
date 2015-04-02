from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
#from django.contrib.auth.views import
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
)


