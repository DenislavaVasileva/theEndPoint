from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from theEndPoint.accounts.views import UserRegisterView, DetailProfileView, EditProfileView

# urlpatterns = [
#     path('register/', UserRegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('profile/<int:pk>/', include([
#         path('details/', DetailProfileView.as_view(), name='profile_details'),
#         path('edit/', EditProfileView.as_view(), name='profile_edit')
#     ])),
# ]
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/details/', DetailProfileView.as_view(), name='profile_details'),  # Current user profile
    path('profile/<int:pk>/details/', DetailProfileView.as_view(), name='profile_details'),  # Edit or other profile
    path('profile/<int:pk>/edit/', EditProfileView.as_view(), name='profile_edit'),
]
