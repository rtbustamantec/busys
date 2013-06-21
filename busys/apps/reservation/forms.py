# coding=utf-8
"""
Copyright (C)

Author:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports
from django import forms

# 3rd party imports

# Local imports
from busys.apps.core.models import Department


class SearchForm(forms.Form):
    departure_date = forms.DateField()
    departure_on = forms.ModelChoiceField(queryset=Department.objects.all())
    arrival_on = forms.ModelChoiceField(queryset=Department.objects.all())

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['departure_date'].widget.attrs['class'] = 'datepicker'

