from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from views import index, test, coffeebeans, blog, product, partnershop, about, logout, account,cart,menu,article
from . import views
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.views import password_change


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
    url(r'^account_allauth/',include('allauth.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    # url(r'^register/', include('registration.backends.hmac.urls')),
    url(r'^cart/$',cart),
    url(r'^menu/$',menu),
    url(r'^article/$',article),
    # url(r'^accounts/login/$',login),
    url(r'^blog', views.BlogIndex.as_view(), name="blog"),
    # url(r"^signup/$", allauth.account.views.SignupView, name="account_allath_signup"),
    url(r"^account_reset_password/$", password_change,
        name="account_allath_change_password"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
