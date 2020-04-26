from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1),
    path('login/', views.login),
    path('logout/', views.logout),
    path('index/', views.index),
    path('yh/', views.yh),
    path('cs1/', views.cs1,name='cs1'),
    path('cs2/', views.cs2,name='cs2'),
    path('cs3/', views.cs3,name='cs3'),
    path('cs4/', views.cs4,name='cs4'),
    path('cs/',views.cs,name='cs'),
    path('cs_new/',views.cs_new,name='cs_new'),
    path('dg/', views.dg),
    path('dg_list/', views.dg_list),
    path('dg_new/', views.dg_new, name='dg_new'),
    path('dg_dc/', views.export_excel, name='dg_dc'),
    path('updatedg/<int:pk>/',views.updatedg,name='updatedg'),
    path('cs_edit/',views.cs_edit,name='cs_edit1'),
    path('cs_edit/<int:pk>/',views.cs_edit,name='cs_edit')
    ]
