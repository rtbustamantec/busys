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
    # Examples:
    #url(r'^$', 'project.views.home', name='home'),
    #url(r'^project/', include('project.foo.urls')),
    '',
    url(r'^reservation/', include('busys.apps.reservation.urls')),
    url(r'^account/', include('busys.apps.account.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
