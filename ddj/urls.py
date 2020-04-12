from django.urls import path 
from . import views

urlpatterns = [
    path('',views.ddj_list,name='ddj_list'),
    ]
