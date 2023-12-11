from django.urls import path
from .views import power_sports

urlpatterns = [
    path('',power_sports, name='ps'),
    path('about/',power_sports, name='ps'),
]