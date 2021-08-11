from ytapi.models import Songs
from knox import views as knox_views
from .views import LoginAPI, SongList, Songss
from django.urls import path
from .views import RegisterAPI
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/songs/<int:pk>/', views.Songss, name='song'),
    path('api/songs/', views.SongList, name='songs'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

