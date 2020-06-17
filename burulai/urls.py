from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import Home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns





urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('apps.chat.urls')),
    path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name='home' ),
    path('categories/', include('apps.blog.urls')),
    path('events/', include('apps.events.urls')),
    path('quiz/' ,include('apps.quiz.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
