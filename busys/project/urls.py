# coding=utf-8
"""
Copyright (C)

Authors:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin

# 3rd party imports

# Local imports


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^reservation/', include('apps.reservation.urls')),
    url(r'^account/', include('apps.account.urls')),
    # Examples:
    #url(r'^$', 'project.views.home', name='home'),
    #url(r'^project/', include('project.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)
