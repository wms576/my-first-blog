from django.conf import settings
from django.db import models
from django.utils import timezone

class Yh(models.Model):
    yhh=models.CharField(max_length=6,verbose_name="用户号")
    yhm=models.CharField(max_length=40,default='用户名',unique=True,verbose_name="用户名")
    mm=models.CharField(max_length=10,verbose_name="密码")
    scdl=models.DateTimeField(default=timezone.now,verbose_name="上次登录时间")
    yhlb=models.CharField(max_length=10,choices=(('客户','客户'),('操作','操作'),('管理','管理'),),verbose_name="用户类别")

    def __str__(self):
        return self.yhm

class Cs(models.Model):
    csm=models.CharField(max_length=100,verbose_name='参数名')
    csz=models.CharField(max_length=100,verbose_name='参数值')
    csh=models.SmallIntegerField(verbose_name='序号')
    def __str__(self):
        return self.csz


class Dg(models.Model):
    yhm=models.CharField(max_length=100,verbose_name='订户名')
    pm=models.CharField(max_length=100,verbose_name='品名')
    cd=models.CharField(max_length=100,verbose_name='产地')
    kz=models.CharField(max_length=100,verbose_name='克重')
    cc=models.CharField(max_length=100,verbose_name='尺寸')
    sl=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    pe=models.CharField(max_length=10,choices=(("单PE","单PE"),("双PE","双PE")),default="单PE")
    xdrq=models.DateTimeField(default=timezone.now,verbose_name='下单时间')
    bz=models.CharField(max_length=200,verbose_name='备注')
    jd=models.BooleanField(default='false',verbose_name='接单')
    wd=models.BooleanField(default='false',verbose_name='完单')
    
    
    
