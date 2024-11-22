from django.shortcuts import render
from django.views.generic import ListView
from theEndPoint.peaks.models import Peak


class PeakListView(ListView):
    model = Peak
    template_name = 'peaks/peaks_dashboard.html'
    context_object_name = 'peaks'
    ordering = ['-elevation']

