from django.urls import path, include
from PowerSports import views
from .views import user_login, register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', user_login, name='login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete'),

    path('register/', register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('single_blog/', views.single_blog, name='single_blog'),
    path('Tennis/', views.tennis, name='Tennis'),
    path('Football/', views.footbal, name='Football'),
    path('Voleyball/', views.voleyball, name='Voleyball'),
    path('Basketball/', views.basketball, name='Basketball'),
]
