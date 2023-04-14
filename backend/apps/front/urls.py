from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('vf4/', views.vf4, name="vf4"),
    path('vf2/', views.vf2, name="vf2"),
    path('st35/', views.st35, name="st35"),
    path('laser/', views.laser, name="laser"),
]