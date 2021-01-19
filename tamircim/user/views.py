
from django.urls import path
from .forms import RegisterForm,LoginForm,arizaform

from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import ariza1
from .models import *
from .forms import *

from django.contrib import messages
# Create your views here.



def acikarizalar(request):
    form = filterForm()
    arizalar = ariza1.objects.all()
    if request.method == "POST":
        form = filterForm(request.POST)
        if form.is_valid():
                arizalar = ariza1.objects.filter(sehir=form.cleaned_data['sehir'], mahalle=form.cleaned_data['mahalle'], ariza=form.cleaned_data['ariza'])

    context = {'form': form, 'arizalar': arizalar}
    return render(request,"acikarizalar.html", context)

def map(request):
  return render(request,"map.html")

def updateProfile(request):
  return render(request,"updateProfile.html")

def mesajlarım(request):
  return render(request,"mesaj.html")

def arizaDetay(request):
  return render(request,"arizadetay.html")


  
def arizaolustur(request):

    form = arizaform(request.POST)
    if request.method=="POST":
       form = arizaform(request.POST)
       if form.is_valid():
         sehir=request.POST['sehir']
         mahalle=request.POST['mahalle']
         ariza=request.POST['ariza']
         tamirci=request.POST['tamirci']
         arizadetay=request.POST['arizadetay']
         userr=request.user
         newariza=ariza1(user=userr,sehir=sehir,mahalle=mahalle,ariza=ariza,tamirci=tamirci,arizadetay=arizadetay)
         newariza.save()
         return redirect("homePage")

    context = {"form":form}
    return render(request,"arizaolustur.html",context)



def register(request):

    form = RegisterForm(request.POST or None)  # burda post yada get mi diye kontrol ediyor
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.info(request,"Başarıyla Kayıt Oldunuz...")
        return redirect("homePage")
    context = {"form":form} # burası post değil ve ife (post ise ife girer) girmemişse
    return render(request,"register.html",context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password) # import ettik (authenticate)

        if user is None: # user yok ise
            messages.info(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user) # import ettiğimiz login
        return redirect("homePage")

    return render(request,"login.html",context)  # form valid değilse burası çalışır

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("homePage")

def homePage(request):
  return render(request,"homePage.html")

def aboutUs(request):
  return render(request,"aboutUs.html")

def mesajj(request):
    return render(request,"mesajj.html")

def forgotPassword(request):
  return render(request,"forgotPassword.html")

def profile(request):
    return render(request, "profile.html")