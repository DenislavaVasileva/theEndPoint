from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        peak = self.object
        total_interest = peak.wished_by.count()
        context['total_interest'] = total_interest
        return context


@login_required
def add_to_wishlist(request, peak_id):
    peak = get_object_or_404(Peak, pk=peak_id)
    profile = request.user.profile

    if peak in profile.wish_list.all():
        message = f'{peak.name} is already in your wish list.'
        context = {
            'peak': peak,
            'profile': profile,
            'message': message,
        }
        return render(request, 'peaks/peak_details.html', context)
    else:
        profile.wish_list.add(peak)
        return redirect('peaks_dashboard')


@login_required
def remove_from_wishlist(request, peak_id):
    peak = get_object_or_404(Peak, pk=peak_id)
    profile = request.user.profile

    if peak in profile.wish_list.all():
        profile.wish_list.remove(peak)
        message = f'{peak.name} is removed from your wish list.'
    else:
        message = f'{peak.name} is not in your wish list.'

    context = {
        'message_remove': message,
        'peak': peak,
        'profile': profile,
    }

    return render(request, 'peaks/peak_details.html', context)
