
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment'),
    url(r'^(?P<article_id>[0-9]+)/keep/$', views.get_keep, name='keep'), 
    url(r'^(?P<article_id>[0-9]+)/poll/$', views.get_poll_article, name='poll'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article'),
 
]
