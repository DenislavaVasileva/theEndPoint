from django.urls import path, include
from theEndPoint.peaks.views import PeakListView, PeakDetailView

urlpatterns = [
    path('', PeakListView.as_view(), name='peaks_dashboard'),
    path('<int:peak_id>/', include([
        path('details/', PeakDetailView.as_view(), name='details-peak'),
    ]))
]

