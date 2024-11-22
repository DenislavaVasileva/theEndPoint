from django.urls import path
from theEndPoint.peaks.views import PeakListView

urlpatterns = [
    path('', PeakListView.as_view(), name='peaks_dashboard'),
]
