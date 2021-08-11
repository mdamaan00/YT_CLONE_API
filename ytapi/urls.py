from ytapi.models import Songs

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [

    path('api/songs/<int:pk>/', views.Songss, name='song'),
    path('api/songs/', views.SongList, name='songs'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

