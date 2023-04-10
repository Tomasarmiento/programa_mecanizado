from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('timer/', views.timer, name="timer"),
    path('laser/', views.laser, name="laser"),
]