from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

from twitter.registeruser.views import register_page,custom_login

urlpatterns = patterns('',
                       (r'^register/$', register_page),
                       (r'^register/success/$', direct_to_template,
                            {'template': 'registration/register_success.html'}),
                       url(r'^login/$', custom_login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}, name='auth_login'),
)