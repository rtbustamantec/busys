# coding=utf-8
"""
Copyright (C)

Author:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports
from django.conf.urls import patterns, url

# 3rd party imports

# Local imports
from apps.reservation.views import ReservationHomePage, ScheduleList


urlpatterns = patterns(
    '',
    url(r'^$', ReservationHomePage.as_view(), name='home'),
    url(r'^schedule/$', ScheduleList.as_view(), name='schedule'),
)
