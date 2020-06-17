from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='chat'),
    path('<str:room_name>/', views.room, name='room'),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)