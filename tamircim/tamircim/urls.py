"""tamircim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('arizaolustur/', views.arizaolustur,name="arizaolustur"),
    path('acikarizalar/', views.acikarizalar,name="acikarizalar"),
    path('map/', views.map,name="map"),
    path('updateProfile/', views.updateProfile,name="updateProfile"),
    path('mesajlarım/', views.mesajlarım,name="mesajlarım"),
    path('arizaDetay/', views.arizaDetay,name="arizaDetay"),
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('homePage/', views.homePage,name="homePage"),
    path('aboutUs/', views.aboutUs,name="aboutUs"),
     path('mesajj/', views.mesajj,name="mesajj"),
]
