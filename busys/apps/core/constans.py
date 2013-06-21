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
from busys.apps.core import strings as core_strings


SEAT_STATE_AVAILABLE = ''
SEAT_STATE_SELECTED = ''
SEAT_STATE_BOOKED = ''
SEAT_STATE_IN_CAR = ''
SEAT_STATE_NOT_AVAILABLE = ''

SEAT_STATE_CHOICES = (
    (SEAT_STATE_AVAILABLE, core_strings.AVAILABLE),
    (SEAT_STATE_SELECTED, core_strings.SELECTED),
    (SEAT_STATE_BOOKED, core_strings.BOOKED),
    (SEAT_STATE_IN_CAR, core_strings.IN_CAR),
    (SEAT_STATE_NOT_AVAILABLE, core_strings.NOT_AVAILABLE),
)

