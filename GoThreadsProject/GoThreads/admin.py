from django.contrib import admin
from .models import Company,Vehicle,Doctor, ShoppingCompany, ResortCompany, BusCompany, AirCompany, ServicesCompany, BabyCareCompany, OnlineCoursesCompany, LifestyleCompany, MedicalCompany, HotelCompany, CarCompany

# Register your models here.
admin.site.register(Company)
admin.site.register(ShoppingCompany)
admin.site.register(ResortCompany)
admin.site.register(BusCompany)
admin.site.register(AirCompany)
admin.site.register(ServicesCompany)
admin.site.register(BabyCareCompany)
admin.site.register(OnlineCoursesCompany)
admin.site.register(LifestyleCompany)
admin.site.register(MedicalCompany)
admin.site.register(HotelCompany)
admin.site.register(CarCompany)
admin.site.register(Vehicle)
admin.site.register(Doctor)
