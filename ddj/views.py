from django.shortcuts import render
from .models import Ddjw
import random

def ddj_list(request):
    ddjws=Ddjw.objects.filter(zjh=random.randint(1,81))
    return render(request,'ddj/ddj_list.html',{'ddjws':ddjws})
