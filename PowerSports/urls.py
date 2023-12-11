from django.urls import path
from .views import power_sports

urlpatterns = [
    path('',power_sports, name='ps'),
    path('about/',power_sports, name='about'),
    path('blog/', power_sports, name='blog'),
    path('contact/', power_sports, name='contact'),
    path('news/', power_sports, name='news'),
    path('single_blog/', power_sports, name='single_blog'),
    path('team/', power_sports, name='team'),
]