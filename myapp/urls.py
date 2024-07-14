from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('main/', views.main, name='main'),
    path('difficulty/', views.difficulty, name='difficulty'),
    path('sound/', views.sound, name='sound'),
    path('text/', views.text, name='text'),
    path('themes/', views.themes, name='themes'),
    path('difficulty/<str:level>/', views.difficulty_level, name='difficulty_level'),
    path('themes/<str:theme>/', views.theme_selection, name='theme_selection'),
    path('my-login', views.my_login, name="login"),
]