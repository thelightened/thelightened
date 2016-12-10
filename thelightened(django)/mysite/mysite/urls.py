from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from cafe.views import index, test, coffeebeans, blog, product, partnershop, about, indexrequest, logout, register, account


urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^indexrequest/$',indexrequest),
    url(r'^logout/$',logout),
    url(r'^indexregister/$',register),
	url(r'^coffeebeans/$',coffeebeans),
    url(r'^blog/$',blog),	
    url(r'^product/$',product),
    url(r'^about/$',about),
    url(r'^partnershop/$',partnershop),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^account/$',account),

    # url(r'^fblog/$',fblog),
    # url(r'^', include('cafe.urls'),
)
