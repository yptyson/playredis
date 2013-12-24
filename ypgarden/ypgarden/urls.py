from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ypgarden.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^company/',include('company.urls')),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_PATH}),
    url(r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_PATH}),
    url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_PATH}),
)
