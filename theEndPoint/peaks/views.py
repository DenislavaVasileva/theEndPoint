from django.views.generic import ListView, DetailView
from theEndPoint.peaks.models import Peak


class PeakListView(ListView):
    model = Peak
    template_name = 'peaks/peaks_dashboard.html'
    context_object_name = 'peaks'
    ordering = ['-elevation']


class PeakDetailView(DetailView):
    model = Peak
    template_name = 'peaks/peak_details.html'
    pk_url_kwarg = 'peak_id'

