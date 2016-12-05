from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
    url(r'^$', 'cafe.views.index', name='index'),
    # url(r'^v1/$', 'my_app.views.v1', name='name_1'),
    # url(r'^v2/$', 'my_app.views.v2', name='name_2'),
    # url(r'^v3/$', 'my_app.views.v3', name='name_3'),
)