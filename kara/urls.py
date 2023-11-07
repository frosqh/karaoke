from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_theme, name='choose_theme'),
    path('theme/<int:pk>/', views.choose_song, name='choose_song'),
    path('reset', views.reset, name='reset')
]
