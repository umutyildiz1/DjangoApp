from django.shortcuts import render
from django.urls import path
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

def login(request):
  return render(request,"login.html")

def register(request):
  return render(request,"register.html")

def homePage(request):
  return render(request,"register.html")