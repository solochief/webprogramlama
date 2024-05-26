"""
URL configuration for hospitalweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from coreapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('adminhesap/', views.admin_account, name='admin_account'),
    path('doktorhesap/', views.doctor_account, name='doctor_account'),
    path('hastahesap/', views.hasta_account, name='hasta_account'),
    path('hasta_ekle/', views.hasta_ekle, name='hasta_ekle'),
    path('doktor_ekle/', views.doktor_ekle, name='doktor_ekle'),
    path('hasta-goruntule/', views.hasta_goruntule, name='hasta_goruntule'),
    path('hasta-sil/', views.hasta_sil, name='hasta_sil'),
    path('doktor-goruntule/', views.doktor_goruntule, name='doktor_goruntule'),
    path('doktor-sil/', views.doktor_sil, name='doktor_sil'),
    path('update-hasta/', views.update_hasta, name='update_hasta'),
    path('dr-hasta-goruntule/', views.dr_hasta_goruntule, name='dr_hasta_goruntule'),
    path('hasta-detay/<int:hasta_id>/', views.hasta_detay, name='hasta_detay'),
    path('hakkimizda/', views.hakkimizda_view, name='hakkimizda_view'),
    path('iletisim/', views.iletisim_view, name='iletisim_view'),
    
    path('admin-doktor/', views.admin_doktor_view, name='admin_doktor_view'),
    path('admin-hasta/', views.admin_hasta_view, name='admin_hasta_view'),
    path('admin-rapor/', views.admin_rapor_view, name='admin_rapor_view'),
    path('admin-randevu-goruntule/', views.admin_randevu_goruntule, name='admin_randevu_goruntule'),
    path('admin-randevu-ekle/', views.admin_randevu_ekle, name='admin_randevu_ekle'),
    path('admin-randevu-guncelle/<int:randevu_id>/', views.admin_randevu_guncelle, name='admin_randevu_guncelle'),
    path('admin-randevu-guncelle/<int:randevu_id>/post/', views.admin_randevu_guncelle_post, name='admin_randevu_guncelle_post'),
    path('admin-randevu-sil/<int:randevu_id>/', views.admin_randevu_sil, name='admin_randevu_sil'),
    path('admin-rapor-goruntule/', views.admin_rapor_goruntule, name='admin_rapor_goruntule'),
    # path('admin-rapor-ekle/', views.admin_rapor_ekle, name='admin_rapor_ekle'),
    path('admin-rapor-guncelle/<int:rapor_id>/', views.admin_rapor_guncelle, name='admin_rapor_guncelle'),
    path('admin-rapor-sil/<int:rapor_id>/', views.admin_rapor_sil, name='admin_rapor_sil'),

    path('doktor-hasta/', views.doktor_hasta_view, name='doktor_hasta_view'),
    # path('doktor_rapor_ekle/<int:hastaID>/', views.doktor_rapor_ekle, name='doktor_rapor_ekle'),
    path('doktor_rapor_goruntule/<int:hastaID>/', views.doktor_rapor_goruntule, name='doktor_rapor_goruntule'),

    
    path('hasta-randevu/', views.hasta_randevu_view, name='hasta_randevu_view'),
    path('get-doktorlar/', views.get_doktorlar, name='get_doktorlar'),
    path('get-randevu-tarihleri/', views.get_randevu_tarihleri, name='get_randevu_tarihleri'),
    path('get-randevu-saatleri/', views.get_randevu_saatleri, name='get_randevu_saatleri'),
    path('randevu-ekle/', views.randevu_ekle_view, name='randevu_ekle'),
    # path('hasta_rapor_ekle/', views.hasta_rapor_ekle, name='hasta_rapor_ekle'),
    path('hasta-rapor/', views.hasta_rapor, name='hasta_rapor'),
    path('get_rapor_json/<int:rapor_id>/', views.get_rapor_json, name='get_rapor_json'),


    ]
