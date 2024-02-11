from django.urls import path, include
from PowerSports import views
from .views import user_login, register
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('single_blog/', views.single_blog, name='single_blog'),
    path('Tennis/', views.tennis, name='Tennis'),
    path('Football/', views.footbal, name='Football'),
    path('Voleyball/', views.voleyball, name='Voleyball'),
    path('Basketball/', views.basketball, name='Basketball'),
    # path('register/', views.register, name='register')
]
