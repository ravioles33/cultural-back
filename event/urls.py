# Djagno imports
from django.urls import path

# Local imports
from event import views

urlpatterns = [
    path(r'event/', views.EventView.as_view(), name='event'),
]