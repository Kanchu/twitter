from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
#from registeruser.forms import RegistrationForm

admin.autodiscover()
from twitter.registeruser.views import register_page

urlpatterns = patterns('',
                       (r'^register/$', register_page),

)