# coding=utf-8
"""
Copyright (C)

Author:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports
from django.contrib import admin

# 3rd party imports
from apps.core.models import Department, Company, Agency, Buss
from apps.core.models import ServiceType, Rate, Schedule

# Local imports


admin.site.register(Department)
admin.site.register(Company)
admin.site.register(Agency)
admin.site.register(Buss)
admin.site.register(ServiceType)
admin.site.register(Rate)
admin.site.register(Schedule)