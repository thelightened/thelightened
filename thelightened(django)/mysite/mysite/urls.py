from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import here
from cafe.views import index, test

urlpatterns = patterns('',
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/',here),
    url(r'^index/$',index),
    url(r'^test/$',test)
)
