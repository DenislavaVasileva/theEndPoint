from django.urls import path, include
from theEndPoint.home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
