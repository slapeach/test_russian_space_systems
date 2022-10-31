from django.contrib import admin
from django.urls import path

from api.views import AlbumView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AlbumView.as_view(), name='albums'),
]
