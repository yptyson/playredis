#-*- coding: utf-8 -*-
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
urlpatterns = patterns('company.views',
    url(r'new/$', 'new'),
    url(r'show/$', 'show'),
    url(r'save/$', 'save'),
    url(r'details/$', 'details'),
    url(r'edit/$', 'edit'),
    url(r'update/$','update'),
    url(r'play/$','play'),
    url(r'play2/$','play2'),
    url(r'query_/$','query_'),
    url(r'query/$','query'),
    url(r'cut/$','cut'),
    url(r'filter_by/$','filter_by'),
    url(r'filter/$','filter'),
    url(r'doublef/$','doublefilter'),
    url(r'likef/$','likefilter'),
    url(r'infi/$','infi'),
    url(r'andf/$','andf'),
    url(r'orf/$','orf'),
    url(r'orlist/$','orlist'),
    url(r'para/$','para'),
    url(r'psql/$','psql'),
    url(r'ql/$','ql')
)
