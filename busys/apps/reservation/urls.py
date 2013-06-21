# coding=utf-8
"""
Copyright (C)

Author:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports
from django.conf.urls import patterns, include, url


# 3rd party imports
from apps.reservation.views import ReservationHomePage, ScheduleList

# Local imports


urlpatterns = patterns(
    '',
    url(r'^$', ReservationHomePage.as_view(), name='home'),
    url(r'^schedule/$', ScheduleList.as_view(), name='schedule'),
)
