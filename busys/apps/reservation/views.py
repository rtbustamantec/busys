# coding=utf-8
"""
Copyright (C)

Author:
    Raul Bustamante Cruzado <rtbustamantec@gmail.com>
"""
# Standard library imports

# Django imports
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404

# 3rd party imports

# Local imports
from busys.apps.core.models import Schedule
from busys.apps.reservation.forms import SearchForm


class ReservationHomePage(TemplateView):
    template_name = 'reservation/base.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())


class ScheduleList(TemplateView):
    template_name = 'reservation/schedule.html'
    schedule_list = None
    search_form = None

    def get(self, request, *args, **kwargs):
        self.schedule_list = Schedule.objects.all()
        self.search_form = SearchForm()
        return self.render_to_response(self.get_context_data())

    def post(self, request):
        self.search_form = SearchForm(request.POST)
        if self.seach_form.is_valid():
            self.schedule_list = Schedule.objects.filter(
                rate__departure_date=
                self.seach_form.cleaned_data['departure_date'],
                rate__departure_on=
                self.seach_form.cleaned_data['departure_on'],
                rate__arrival_on=self.seach_form.cleaned_data['arrival_on']
            )

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(ScheduleList, self).get_context_data(**kwargs)
        context['schedule_list'] = self.schedule_list
        context['search_form'] = self.seach_form
        return context
