from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from . import models
from .models import Yh,Pm,Dg
from .forms import UserForm,DgForm
from django.http import Http404
def index1(request):
    return redirect('./index/')

def yh(request):
    yhs = Yh.objects.all()
    return render(request,'kst/yh_list.html',{'yhs':yhs})

def dg(request):
    dgs=Dg.objects.filter(yhm=request.session['user_name'])
    return render(request,'kst/dg.html',{'dgs':dgs})

def dg_new(request):
    if request.method=="POST":
        form = DgForm(request.POST)
        if form.is_valid():
            dg=form.save(commit=False)
            dg.yhm=Yh.objects.get(yhm=request.session['user_name'])
            dg.xdrq = timezone.now()
            dg.jd=False
            dg.wd=False
            dg.save()
            return redirect('../dg/')
    else:
        form=DgForm()
        return render(request,'kst/updatedg.html',{'form':form})

def updatedg(request,pk):
    dg=get_object_or_404(Dg,pk=pk)
    if request.method=="POST":
        form = DgForm(request.POST,instance=dg)
        if form.is_valid():
            dg=form.save(commit=False)
            dg.xdrq = timezone.now()
            dg.save()
            dgs = Dg.objects.filter(yhm=request.session['user_name'])
            #**return render(request, 'kst/dg.html', {'dgs': dgs})
            return redirect('../../dg/')
    else:
        form=DgForm(instance=dg)
        return render(request,'kst/updatedg.html',{'form':form})


def index(request):
    return render(request,'kst/index.html')

def login(request):
    if request.method == "POST":
        login_form=UserForm(request.POST)
        message="请检查填写内容"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Yh.objects.get(yhh=username)
                if user.mm ==password:
                    request.session['is_login']=True
                    request.session['user_name']=user.yhm
                    request.session['user_yhlb']=user.yhlb
                    return redirect('../index/')
                else:
                    message="密码不正确"
            except:
                message="用户号不存在"
                return render (request,'kst/login.html',locals())
    login_form=UserForm()
    return render(request,'kst/login.html',locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('../index/')
    request.session.flush()
    return redirect('../index/')

def pm(request):
    if request.method == "POST":
        if request.POST['pm'] == '':
            return render(request,"kst/pm.html",{'alert':'请输入内容！'})
        else:
            a_row=Pm(pm=request.POST['pm'])
            a_row.save()
            content={'list':Pm.objects.all()}
            return render(request,"kst/pm.html",content)
    elif request.method=='GET':
        content={'list':Pm.objects.all()}
        return render(request,"kst/pm.html",content)