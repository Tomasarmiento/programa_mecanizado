from django.urls import path, re_path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('nesting_select/', views.nesting_select, name='nesting_select'),
    path('piece_select/', views.piece_select, name='piece_select'),
    path('timer_vf4/', views.timer_vf4, name='timer_vf4'),
    # path('timer_vf4/', views.StartRoutine.as_view(), name='timer_vf4'),
    path('finish_start_vf4/', views.finish_start_vf4, name='finish_start_vf4'),
    path('selected_piece/', views.selected_piece, name='selected_piece'),
    path('msg_pause/', views.msg_pause, name='msg_pause'),
    path('msg_ss/', views.msg_ss, name='msg_ss'),
    path('send_ss/', views.send_ss, name='send_ss'),
    path('finishCicle/', views.finish_cicle, name='finish_cicle'),
]