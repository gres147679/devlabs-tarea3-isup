from django.conf.urls import patterns, url

from isUp import views

urlpatterns = patterns('',
    url(r'^$', views.scan, name='scan'),
    url(r'^results', views.scan, name='results')
)