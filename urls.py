from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
import settings
from views import logout_page,welcome,tweet,list_tweet, switch_language


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'twitter.views.home', name='home'),
    (r'', include('twitter.registeruser.urls')),
    (r'^switch/(?P<language>.{2}?)/$', switch_language),
    (r'^logout/$', logout_page),
    (r'^welcome$',welcome),
    (r'^tweet/$', tweet),
    (r'^list_tweet/$', list_tweet),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
