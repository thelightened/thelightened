from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login,indexhomepage,logout
from django.conf import settings
from cafe.views import index, test, coffeebeans,blog

urlpatterns = patterns('',
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^test/$',test),
    url(r'^login/$',login),
    url(r'^logout/$',logout),
	url(r'^coffeebeans/$',coffeebeans),
    url(r'^indexhomepage/$',indexhomepage),	
    url(r'^blog/$',blog),	
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
)
