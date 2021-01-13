from django.shortcuts import render
from django.urls import path
from .forms import RegisterForm,LoginForm

from django.shortcuts import render,redirect



from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

from django.contrib import messages
# Create your views here.


def arizaolustur(request):
  return render(request,"arizaolustur.html")

def acikarizalar(request):
  return render(request,"acikarizalar.html")

def map(request):
  return render(request,"map.html")

def updateProfile(request):
  return render(request,"updateProfile.html")

def mesajlarım(request):
  return render(request,"mesaj.html")

def arizaDetay(request):
  return render(request,"arizadetay.html")



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
  return render(request,"profile.html")