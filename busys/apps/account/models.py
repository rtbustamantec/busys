# coding=utf-8
"""
Copyright (C)

Author:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports
from django.contrib.auth.models import User
from django.db import models

# 3rd party imports

# Local imports
from apps.core.models import Company
from apps.account.constants import IDENTIFICATION_TYPE_CHOICES


class UserProfile(models.Model):
    company = models.ForeignKey(Company)
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    identification_type = models.ForeignKey(
        max_length=3, choices=IDENTIFICATION_TYPE_CHOICES
    )
    identification_number = models.IntegerField(
        max_length=8, null=False, blank=False
    )
    birthday = models.DateField()
    nationality = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=20)






