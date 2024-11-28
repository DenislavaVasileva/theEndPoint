from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from theEndPoint.accounts.views import RegisterUserView, DetailProfileView, EditProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/details/', DetailProfileView.as_view(), name='profile_details'),
    path('profile/<int:pk>/edit/', EditProfileView.as_view(), name='profile_edit'),
]
