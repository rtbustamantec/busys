# -*- coding: utf-8 -*-
"""

Copyrigh (C) 2013

Authors:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports

# 3rd party imports

# Local imports
from apps.account import strings as account_strings


IDENTIFICATION_TYPE_DNI = 'DNI'
IDENTIFICATION_TYPE_PASSPORT = 'PASS'

IDENTIFICATION_TYPE_CHOICES = (
    (IDENTIFICATION_TYPE_DNI, account_strings.IDENTIFICATION_TYPE_DNI),
    (IDENTIFICATION_TYPE_PASSPORT, account_strings.IDENTIFICATION_TYPE_PASSPORT)
)

#CACHE CONSTANTS
CACHE_USER = "%i:user:%i"
USERNAME_MAX_LENGTH = 29
STATUS_MAX_LENGTH = 140