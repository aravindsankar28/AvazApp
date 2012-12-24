from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from AwazApp.models import *
from AwazApp.views import *
from dajaxice.core import dajaxice_autodiscover
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
dajaxice_autodiscover()
urlpatterns = patterns('',
    url(r'home/$',"AwazApp.views.home", name='home'),
    url(r'getSearch/$',"AwazApp.views.getSearch", name='getSearch'),
    url(r'upload_file/$',"AwazApp.views.upload_file", name='upload_file'),
    #url(r'images/$',"AwazApp.views.images", name='images'),
    url(r'removeImg/(?P<foobar>.+)/$',"AwazApp.views.removeImg", name='removeImg'),
    url(r'images/$',"AwazApp.views.images", name='images'),
    url(r'imageSearch/(?P<foobar>.+)/$',"AwazApp.views.imageSearch", name='images'),
    url(r'^getChildren/(?P<foobar>.+)/$','AwazApp.views.getChildren',name='getChildren'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'searchupdate/$',"AwazApp.views.searchupdate", name='searchupdate'),
    url(r'test/$',"AwazApp.views.test", name='test'),
    url(r'editsave/$',"AwazApp.views.editsave", name='editsave'),
    url(r'create/$',"AwazApp.views.create", name='create'),
    url(r'audio/$',"AwazApp.views.audio", name='audio'),
    #url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    # url(r'^Awaz/', include('Awaz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
