from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1),
    path('login/',views.login),
    path('logout/',views.logout),
    path('index/',views.index),
    path('yh/',views.yh),
    path('dg/',views.dg),
    path('updatedg/<int:pk>/',views.updatedg,name='updatedg'),

    ]
