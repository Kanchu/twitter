from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template

from twitter.registeruser.views import register_page

urlpatterns = patterns('',
                       (r'^register/$', register_page),
                       (r'^register/success/$', direct_to_template,
                            {'template': 'registration/register_success.html'}),
)