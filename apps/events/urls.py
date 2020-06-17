from django.urls import path
from .views import *


urlpatterns = [
    path('', events_list, name='events_list_url'), 
    path('event/<str:slug>/', event_detail, name='event_detail'),
    path('confirm-event/', confirm , name='event_enroll'),
]
