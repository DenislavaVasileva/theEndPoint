from django.urls import path

from django.contrib.auth.views import (
    LoginView,
    LogoutView)

from theEndPoint.accounts.views import (
    RegisterUserView,
    DetailProfileView,
    EditProfileView,
    DeleteProfileView
)

urlpatterns = [
    # Authentication URLs
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Profile URLs
    path('profile/<int:pk>/details/', DetailProfileView.as_view(), name='profile_details'),
    path('profile/<int:pk>/edit/', EditProfileView.as_view(), name='profile_edit'),
    path('profile/<int:pk>/delete/', DeleteProfileView.as_view(), name='profile_delete'),
]
