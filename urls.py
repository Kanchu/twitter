from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from views import logout_page


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'twitter.views.home', name='home'),
    (r'', include('twitter.registeruser.urls')),
#    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # url(r'^twitter/', include('twitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
