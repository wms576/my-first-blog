from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1),
    path('login/', views.login),
    path('logout/', views.logout),
    path('index/', views.index),
    path('yh/', views.yh),
    path('yh_new/', views.yh_new, name='yh_new'),
    path('yh_delete/<int:pk>/', views.yh_delete, name='yh_delete'),
    path('yh_edit/', views.yh_edit, name='yh_edit1'),
    path('yh_edit/<int:pk>/', views.yh_edit, name='yh_edit'),
    path('yh_editmm/<int:pk>',views.yh_editmm,name='yh_editmm'),

    path('cs1/', views.cs1,name='cs1'),
    path('cs2/', views.cs2,name='cs2'),
    path('cs3/', views.cs3,name='cs3'),
    path('cs4/', views.cs4,name='cs4'),
    path('cs/',views.cs,name='cs'),
    path('cs_new/',views.cs_new,name='cs_new'),
    path('cs_delete/<int:pk>/',views.cs_delete,name='cs_delete'),
    path('cs_edit/', views.cs_edit, name='cs_edit1'),
    path('cs_edit/<int:pk>/', views.cs_edit, name='cs_edit'),

    path('dg/', views.dg),
    path('dg_list/', views.dg_list),
    path('dg_new/', views.dg_new, name='dg_new'),
    path('dg_dc/', views.export_excel, name='dg_dc'),
    path('dg_jd/<int:pk>/',views.dg_jd,name='dg_jd'),
    path('dg_delete/<int:pk>/',views.dg_delete,name='dg_delete'),
    path('updatedg/<int:pk>/',views.updatedg,name='updatedg'),

    ]
