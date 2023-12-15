from django.urls import path
from PowerSports import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('single_blog/', views.single_blog, name='single_blog'),
    path('team/', views.team, name='team'),
    path('register/', views.register, name='register')
]
