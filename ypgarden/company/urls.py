#-*- coding: utf-8 -*-
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
urlpatterns = patterns('company.views',
    url(r'new/$', 'new'),
    url(r'show/$', 'show'),
    url(r'save/$', 'save'),
    url(r'details/$', 'details'),
    url(r'edit/$', 'edit'),
    url(r'update/$','update')
)
