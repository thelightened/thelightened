from django.conf.urls import patterns, url
# from django.contrib import admin
from django.conf import settings
from views import index, test, coffeebeans, blog, product, partnershop, about, logout, account,RegisterView,cart,menu,article
from . import views
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^index/$',views.index, name='index'),
    url(r'^logout/$',logout),
    url(r'^register/$',RegisterView.as_view(), name='register'),
	url(r'^coffeebeans/$',coffeebeans),
    url(r'^blog/$',blog),	
    url(r'^product/$',product),
    url(r'^about/$',about),
    url(r'^partnershop/$',partnershop),
    url(r'^account/$',account),
    url(r'^cart/$',cart),
    url(r'^menu/$',menu),
    url(r'^article/$',article),
    # url(r'^accounts/login/$',login),
    url(r'^blog', views.BlogIndex.as_view(), name="blog"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
