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

class Pm(models.Model):
    pm=models.CharField(max_length=100,verbose_name="品名")
    def __str__(self):
        return self.pm

class Cd(models.Model):
    cd=models.CharField(max_length=100,verbose_name="产地")
    def __str__(self):
        return self.cd

class Kz(models.Model):
    kz=models.CharField(max_length=100,verbose_name="克重")
    def __str__(self):
        return self.kz

class Cc(models.Model):
    cc=models.CharField(max_length=100,verbose_name="尺寸")
    def __str__(self):
        return self.cc

    
class Dg(models.Model):
    yhm=models.ForeignKey(to=Yh,to_field='yhm',on_delete=models.DO_NOTHING,verbose_name='订户名')
    pm=models.ForeignKey(Pm,on_delete=models.DO_NOTHING,verbose_name='品名')
    cd=models.ForeignKey(Cd,on_delete=models.DO_NOTHING,verbose_name='产地')
    kz=models.ForeignKey(Kz,on_delete=models.DO_NOTHING,verbose_name='克重')
    cc=models.ForeignKey(Cc,on_delete=models.DO_NOTHING,verbose_name='尺寸')
    sl=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    pe=models.CharField(max_length=10,choices=(("单PE","单PE"),("双PE","双PE")),default="单PE")
    xdrq=models.DateTimeField(default=timezone.now,verbose_name='下单时间')
    bz=models.CharField(max_length=200,verbose_name='备注')
    jd=models.BooleanField(default='false',verbose_name='接单')
    wd=models.BooleanField(default='false',verbose_name='完单')
    
    
    
