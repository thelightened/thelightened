"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from cafe import urls
#oscar



# from cafe.views import index, test, coffeebeans, blog, product, partnershop, about, indexrequest, logout, register, account


urlpatterns = [
    # url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
 #    url(r'^index/$',index),
 #    url(r'^indexrequest/$',indexrequest),
 #    url(r'^logout/$',logout),
 #    url(r'^indexregister/$',register),
	# url(r'^coffeebeans/$',coffeebeans),
 #    url(r'^blog/$',blog),	
 #    url(r'^product/$',product),
 #    url(r'^about/$',about),
 #    url(r'^partnershop/$',partnershop),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    # url(r'^account/$',account),
    # url(r'^markdown/', include("django_markdown.urls")),
    # url(r'^fblog/$',fblog),
    url(r'', include('cafe.urls')),
    # url(r'^checkout/paypal/', include('paypal.express.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

