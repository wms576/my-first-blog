from django import forms
from .models import *


class CsForm(forms.ModelForm):

    class Meta:
        model=Cs
        fields=('csz','csh',)

class YhForm(forms.ModelForm):
    Choicesyhlb = (('管理', '管理'), ('操作', '操作'), ('客户', '客户'),)
    yhlb=forms.ChoiceField(choices=Choicesyhlb,label='用户类别')
    class Meta:
        model=Yh
        fields=('yhh','yhm','yhlb','mm')

class YhForm1(forms.ModelForm):
    Choicesyhlb = (('操作', '操作'), ('客户', '客户'),)
    yhlb=forms.ChoiceField(choices=Choicesyhlb,label='用户类别')
    class Meta:
        model=Yh
        fields=('yhh','yhm','yhlb','mm')

class YhmmForm(forms.ModelForm):
    Choicesyhlb = (('客户', '客户'),)
    yhlb=forms.ChoiceField(choices=Choicesyhlb,label='用户类别')
    class Meta:
        model=Yh
        fields=('yhlb','mm')

class DgForm(forms.ModelForm):

    cc1 = Cs.objects.filter(csm="品名")
    Choices1 = ((c1.csz, c1.csz) for c1 in cc1)
    pm = forms.ChoiceField(choices=Choices1,label='品名')
    cc1 = Cs.objects.filter(csm="产地")
    Choices2 = ((c1.csz, c1.csz) for c1 in cc1)
    cd = forms.ChoiceField(choices=Choices2,label='产地')
    cc1 = Cs.objects.filter(csm="克重")
    Choices3 = ((c1.csz, c1.csz) for c1 in cc1)
    kz = forms.ChoiceField(choices=Choices3,label='克重')
    cc1=Cs.objects.filter(csm="pe")
    Choices4=((c1.csz,c1.csz) for c1 in cc1)
    pe=forms.ChoiceField(choices=Choices4,label='PE')

    class Meta:
        model=Dg
        fields=('pm','cd','kz','cc','sl','pe','yhrq','bz')


class UserForm(forms.Form):
    username = forms.CharField(label="用户号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))