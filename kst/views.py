from django.utils import timezone
import datetime
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from io import BytesIO
from . import models
from .models import *
from .forms import *
from django.http import Http404
import xlwt

def index1(request):
    return redirect('./index/')

def yh(request):
    yhs = Yh.objects.all()
    return render(request,'kst/yh_list.html',{'yhs':yhs})

def cs1(request):
    request.session['csm']='品名'
    kstcss=Cs.objects.filter(csm='品名')
    return render(request,'kst/cs_list.html',{'kstcss':kstcss})
def cs2(request):
    request.session['csm'] = '产地'
    kstcss=Cs.objects.filter(csm='产地')
    return render(request,'kst/cs_list.html',{'kstcss':kstcss})
def cs3(request):
    request.session['csm'] = '克重'
    kstcss=Cs.objects.filter(csm='克重')
    return render(request,'kst/cs_list.html',{'kstcss':kstcss})
def cs4(request):
    request.session['csm'] = '尺寸'
    kstcss=Cs.objects.filter(csm='尺寸')
    return render(request,'kst/cs_list.html',{'kstcss':kstcss})

def cs(request):
    kstcss = Cs.objects.filter(csm=request.session['csm'])
    return render(request, 'kst/cs_list.html', {'kstcss': kstcss})

def cs_edit(request,pk):
    cs = get_object_or_404(Cs, pk=pk)
    if request.method == "POST":
        form = CsForm(request.POST, instance=cs)
        if form.is_valid():
            cs = form.save(commit=False)
            cs.save()
            # **return render(request, 'kst/dg.html', {'dgs': dgs})
            return redirect('../../cs/')
    else:
        form = CsForm(instance=cs)
        return render(request, 'kst/cs_edit.html', {'form': form})


def cs_new(request):
    if request.method=="POST":
        form = CsForm(request.POST)
        if form.is_valid():
            cs=form.save(commit=False)
            cs.csm=request.session['csm']
            cs.save()
            return redirect('../cs/')
    else:
        form=CsForm()
        return render(request,'kst/cs_edit.html',{'form':form})

def dg(request):
    dgs=Dg.objects.filter(yhm=request.session['user_name'])
    return render(request,'kst/dg.html',{'dgs':dgs})
def dg_list(request):
    dgs=Dg.objects.filter(wd=False)
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
                user = Yh.objects.get(yhh=username)
                if user.mm ==password:
                    request.session['is_login']=True
                    request.session['user_name']=user.yhm
                    request.session['user_yhlb']=user.yhlb
                    request.session['csm']='品名'
                    return redirect('../index/')
                else:
                    message="密码不正确"
            except:
                message="用户号不存在1:*"+username+"*"
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

def export_excel(request):
  dgs=Dg.objects.all()
  # 设置HTTPResponse的类型
  response = HttpResponse(content_type='application/vnd.ms-excel')
  response['Content-Disposition'] = 'attachment;filename=dc.xls'
  """导出excel表"""
  if dgs:
    # 创建工作簿
    ws = xlwt.Workbook(encoding='utf-8')
    # 添加第一页数据表
    w = ws.add_sheet('sheet1') # 新建sheet（sheet的名称为"sheet1"）
    # 写入表头
    w.write(0, 0, u'用户名')
    w.write(0, 1, u'品名')
    w.write(0, 2, u'产地')
    w.write(0, 3, u'尺寸')
    # 写入数据
    excel_row = 1
    for dg in dgs:
      # 写入每一行对应的数据
      w.write(excel_row, 0, dg.yhm)
      w.write(excel_row, 1, dg.pm)
      w.write(excel_row, 2, dg.cd)
      w.write(excel_row, 3, dg.kz)
      w.write(excel_row, 4, dg.cc)
      w.write(excel_row, 5, dg.pe)
      w.write(excel_row, 6, (dg.xdrq+datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'))
      w.write(excel_row, 7, dg.sl)
      w.write(excel_row, 8, dg.bz)

      excel_row += 1
    # 写出到IO
    output = BytesIO()
    ws.save(output)
    # 重新定位到开始
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=test.xls'
    response.write(output.getvalue())
  return response