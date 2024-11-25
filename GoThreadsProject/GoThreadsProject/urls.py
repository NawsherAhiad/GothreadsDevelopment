"""
URL configuration for GoThreadsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from GoThreads.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name = 'home'),
    path('companies/', company_list, name='company_list'),
    path('car-companies/', car_company_list, name='car_company_list'),
    path('vehicles/', vehicle_list, name='vehicle_list'),
    path('hotel-companies/', hotel_company_list, name='hotel_company_list'),
    path('medical-companies/', medical_company_list, name='medical_company_list'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('online-courses-companies/', online_courses_company_list, name='online_courses_company_list'),
    path('resort-companies/', resort_company_list, name='resort_company_list'),
    path('services-companies/', services_company_list, name='services_company_list'),
    path('air-companies/', air_company_list, name='air_company_list'),
    path('bus-companies/', bus_company_list, name='bus_company_list'),
    path('train-companies/', train_company_list, name='train_company_list'),
    path('lifestyle-companies/', lifestyle_company_list, name='lifestyle_company_list'),
    path('shopping-companies/', shopping_company_list, name='shopping_company_list'),
    path('baby-care-companies/', baby_care_company_list, name='baby_care_company_list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
