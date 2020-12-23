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