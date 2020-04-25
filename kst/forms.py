from django import forms
from .models import Dg,Pm

class DgForm(forms.ModelForm):
    pm=forms.ModelChoiceField(queryset=Pm.objects.all())

    class Meta:
        model=Dg
        fields=('pm','cd','kz','cc','sl','pe','bz')

class UserForm(forms.Form):
    username = forms.CharField(label="用户号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))