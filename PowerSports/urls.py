from django.urls import path
from PowerSports import views
from .views import user_login, user_register


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('single_blog/', views.single_blog, name='single_blog'),
    path('team/', views.team, name='team'),
    # path('register/', views.register, name='register')
]
