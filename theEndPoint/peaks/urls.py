from django.urls import path, include

from theEndPoint.peaks.views import (
    PeakListView,
    PeakDetailView,
    add_to_wishlist,
    remove_from_wishlist
)

urlpatterns = [
    path('', PeakListView.as_view(), name='peaks_dashboard'),
    path('<int:peak_id>/', include([
        path('details/', PeakDetailView.as_view(), name='details-peak'),
        path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
        path('remove_from_wishlist/', remove_from_wishlist, name='remove_from_wishlist'),

    ]))
]

