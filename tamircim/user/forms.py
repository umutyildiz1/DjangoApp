from django import forms #django nun kendi içinde form clası var
from django.forms import ModelForm
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullancı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)
    


class RegisterForm(forms.Form):
    
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=10,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=10,label="Parolayı doğrula",widget=forms.PasswordInput)
    email = forms.EmailField(max_length=50)
    USERTYPE = (
        ('kullanıcı', 'Kullanıcı'),
        ('tamirci', 'Tamirci')
    )
    userType= forms.CharField(label='Kullanıcı Tipi', widget=forms.Select(choices=USERTYPE))

   
    def clean(self):   # clean metodunu override ettik djangonun kendi içinde var ( parola kontrol için)
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {
            "username" : username,
            "password" : password
        }
        return values


class arizaform(forms.Form):
    sehir=forms.CharField(max_length=25)
    mahalle=forms.CharField(max_length=25)
    ariza=forms.CharField(max_length=25)
    tamirci=forms.CharField(max_length=25)
    arizadetay=forms.CharField(max_length=250)


class filterForm(ModelForm):
    class Meta:
        model = ariza1
        fields = ['sehir', 'mahalle', 'ariza']
