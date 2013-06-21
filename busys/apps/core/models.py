# coding=utf-8
"""
Copyright (C)

Author:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports
from datetime import datetime

# Django imports
from django.contrib.auth.models import User
from django.db import models

# 3rd party imports

# Local imports
from busys.apps.core.middleware import threadlocals


class AuditableManager(models.Manager):
    """class manager for AuditableModel"""

    def get_query_set(self):
        """
        return ONLY the records with is_delete is false
        """
        return super(AuditableManager, self).get_query_set()\
            .filter(is_delete=False)


class AuditableModel(models.Model):
    """Base class for all models"""
    created_date = models.DateTimeField(
        auto_now_add=True, default=datetime.now(), editable=False
    )
    created_by = models.ForeignKey(
        User, editable=False, null=True,
        related_name="%(class)s_created_related"
    )
    modified_date = models.DateTimeField(
        auto_now=True, editable=False, null=True
    )
    modified_by = models.ForeignKey(
        User, editable=False, null=True,
        related_name="%(class)s_modified_related"
    )
    deleted_date = models.DateTimeField(editable=False, null=True)
    deleted_by = models.ForeignKey(
        User, editable=False, null=True,
        related_name="%(class)s_deleted_related"
    )
    is_delete = models.BooleanField(default=False, editable=False)

    #managers
    objects = models.Manager()
    current = AuditableManager()

    #methods
    def __init__(self, *args, **kwargs):
        super(AuditableModel, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        """save and add auditable fields"""
        """
        If its a new object, set the creation user and assign the url_id
        """
        # If the object already existed, it will already have an id
        if self.id:
            user = threadlocals.get_non_anonymous_user()
            if user.is_staff and hasattr(self, "admined") and \
                    hasattr(self, "admined_by"):
                # This object is being edited by an admin set the admined
                self.admined_by = threadlocals.get_non_anonymous_user()
                self.admined = datetime.now()
            else:
                # This object is being edited, not saved, set last_edited_by
                self.modified_by = threadlocals.get_non_anonymous_user()
        else:
            # This is a new object, set the owner
            self.created_by = threadlocals.get_non_anonymous_user()

        if self.is_delete:
            self.deleted_date = datetime.now()
            self.deleted_by = threadlocals.get_non_anonymous_user()

        super(AuditableModel, self).save(*args, **kwargs)

    def delete(self, force=False, *args, **kwargs):
        """Overrides de delete method to add a logicaly feature"""
        if not self.is_delete:
            self.is_delete = True
            self.save()
            if force:
                super(AuditableModel, self).delete(*args, **kwargs)

    class Meta:
        """Meta class for AuditableModel"""
        abstract = True


class Department(models.Model):
    code = models.CharField(max_length=3, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    ruc = models.CharField(max_length=11, null=False, blank=False)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Agency(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    company = models.ForeignKey(Company, null=True, blank=False)
    departament = models.ForeignKey(Department, null=True, blank=False)

    def __unicode__(self):
        return self.name


class ServiceType(models.Model):
    pass


class Buss(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    company = models.ForeignKey(Company, null=True, blank=False)


class Rate(models.Model):
    company = models.ForeignKey(Company, null=True, blank=False)
    departure_on = models.ForeignKey(Department, null=True, blank=False,
                                     related_name="Departure_related")
    arrival_on = models.ForeignKey(Department, null=True, blank=False,
                                   related_name="Arrival_related")
    departure_date = models.DateField(default=None, blank=True)
    departure_time = models.TimeField(default=None, blank=True)
    arrival_date = models.DateField(default=None, null=True, blank=True)
    arrival_time = models.TimeField(default=None, null=True, blank=True)
    duration = models.FloatField(max_length=5, null=True, blank=True)
    price = models.FloatField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return str(self.departure_on) + "-" + str(self.arrival_on)


class Schedule(models.Model):
    company = models.ForeignKey(Company, null=True, blank=False)
    agency = models.ForeignKey(Agency, null=True, blank=False)
    rate = models.ForeignKey(Rate, null=True, blank=False)

