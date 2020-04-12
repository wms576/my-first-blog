from django.shortcuts import render

def ddj_list(request):
    return render(request,'ddj/ddj_list.html',{})
