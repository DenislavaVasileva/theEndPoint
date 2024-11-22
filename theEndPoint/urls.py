from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from theEndPoint import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theEndPoint.home.urls')),
    path('accounts/', include('theEndPoint.accounts.urls')),
    path('posts/', include('theEndPoint.posts.urls')),
    path('peaks/', include('theEndPoint.peaks.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
