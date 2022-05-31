from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('home', views.home, name="home"),
    path('newschedule', views.newschedule, name='newschedule'),
    path('yourschedule', views.yourschedule, name='yourschedule'),
    path('login', views.login, name='login'),
    path('loginview', views.loginview, name='loginview'),
    path('editschedule', views.editschedule, name='editschedule'),
    path('mentorship', views.mentorship, name='mentorship'),
    path('recomendation', views.recomendation, name='recomendation'),
    path('track', views.track, name='track'),
]