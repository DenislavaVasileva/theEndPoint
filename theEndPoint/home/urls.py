from django.urls import path
from theEndPoint.home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
