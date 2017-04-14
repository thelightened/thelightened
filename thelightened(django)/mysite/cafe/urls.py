from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from views import *
from . import views
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.views import *
from oscar.app import application
urlpatterns = [
    url(r'^$', index),
    url(r'^index/$',views.index, name='index'),
    url(r'^logout/$',logout),
    # url(r'^register/$',RegisterView.as_view(), name='register'),
	url(r'^coffeebeans/$',coffeebeans),
    url(r'^blog/$',blog),	
    url(r'^product/$',product),
    url(r'^about/$',about),
    url(r'^partnershop/$',partnershop),
    url(r'^account/$',account),
    url(r'^allauth/',include('allauth.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^cart/$',cart),
    # url(r'^passwordchange/$',passwordchange),
    url(r'^menu/$',menu),
    url(r'^article/$',article),
    # url(r'^email/$',email),
    # url(r'^accounts/login/$',login),
    
    url(r'^blog', views.BlogIndex.as_view(), name="blog"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'', include(application.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
