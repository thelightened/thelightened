from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login,indexhomepage
from django.conf import settings
from cafe.views import index, test, coffeebeans, blog

urlpatterns = patterns('',
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^test/$',test),
    url(r'^login/$',login),
	# url(r'^coffeebeans/$',coffeebeans),
    url(r'^indexhomepage/$',indexhomepage),	
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^blog/',blog),
)
