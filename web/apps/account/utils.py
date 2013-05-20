# coding=utf-8
"""
Copyright (C)

Author:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports
from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache

# 3rd party imports
from apps.account.constants import CACHE_USER

# Local imports


"""
Utilities for the registration app. Basically Cache Stuff.
"""


def get_cached_user(user_id):
    """ Gets a User object from the Cache, or try to get it from the DB, or
    return a None object if it does not exist. Receives the User Id as the
    parameter.
    """
    user = cache.get(CACHE_USER % (settings.SITE_ID, user_id), None)
    if user is None:
        try:
            user = User.objects.get(pk=user_id)
            cache.set(CACHE_USER % (settings.SITE_ID, user_id), user,
                      settings.DEFAULT_CACHE_TIMEOUT)
        except User.DoesNotExist:
            user = None
    return user