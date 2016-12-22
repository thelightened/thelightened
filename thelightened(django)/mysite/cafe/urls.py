from django.conf.urls import patterns, url
# from django.contrib import admin
# from django.conf import settings
from views import index, test, coffeebeans, blog, product, partnershop, about, logout, register, account
from . import views


urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^index/$',index),
    url(r'^logout/$',logout),
    url(r'^indexregister/$',register),
	url(r'^coffeebeans/$',coffeebeans),
    url(r'^blog/$',blog),	
    url(r'^product/$',product),
    url(r'^about/$',about),
    url(r'^partnershop/$',partnershop),
    url(r'^account/$',account),
    url(r'^blog', views.BlogIndex.as_view(), name="blog"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
