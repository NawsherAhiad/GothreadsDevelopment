from django.db import models

class Company(models.Model):
    COMPANY_TYPES = [
        ('CarCompany', 'Car Company'),
        ('HotelCompany', 'Hotel Company'),
        ('MedicalCompany', 'Medical Company'),
        ('LifestyleCompany', 'Lifestyle Company'),
        ('OnlineCoursesCompany', 'Online Courses'),
        ('BabyCareCompany', 'Baby Care Company'),
        ('ServicesCompany', 'Services Company'),
        ('AirCompany', 'Air Company'),
        ('BusCompany', 'Bus Company'),  
        ('LonchCompany', 'Lonch Company'),
        ('ResortCompany', 'Resort Company'),
        ('ShoppingCompany', 'Shopping Company'),
    ] 
    company_id = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=20, choices=COMPANY_TYPES)
    details = models.TextField(blank=True, max_length=300)  
    location = models.CharField(max_length=200)
    rating = models.FloatField(blank=True, null=True)
   
    def __str__(self):
        return self.company_name


class CarCompany(Company):
    phone = models.CharField(max_length=15) 
    profile_picture = models.ImageField(upload_to='CarCompanyLogo', blank=True, null=True)
    
    def __str__(self):
        return f"Car Company: {self.company_name}"
    

class Vehicle(models.Model):
    car_company = models.ForeignKey(CarCompany, related_name='vehicles', on_delete=models.CASCADE)
    car_model = models.CharField(max_length=100)
    year_of_manufacture = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.car_model} ({self.year_of_manufacture}) - {self.car_company.company_name}"


class HotelCompany(Company):
    phone = models.CharField(max_length=15) 
    room_count = models.IntegerField()
    profile_picture = models.ImageField(upload_to='HotelLogo', blank=True, null=True)


class MedicalCompany(Company):
    open_time = models.TimeField(blank=True, null=True)  
    close_time = models.TimeField(blank=True, null=True) 
    profile_picture = models.ImageField(upload_to='MedicalLogo', blank=True, null=True)
    phone = models.CharField(max_length=15) 

    def __str__(self):
        return f"Medical Company: {self.company_name}"
    

class Doctor(models.Model):  
    medical_company = models.ForeignKey(MedicalCompany, related_name='doctors', on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50)
    education = models.CharField(max_length=200, blank=True, null=True)
    rating = models.FloatField(null=True, blank=True)
    visit_price = models.PositiveIntegerField()
    phone = models.CharField(max_length=15) 

    def __str__(self):
        return f"Dr. {self.doctor_name} - {self.speciality}"


class OnlineCoursesCompany(Company):
    price_range = models.CharField(max_length=50)  
    profile_picture = models.ImageField(upload_to='OnlineCourseLogo', blank=True, null=True)
    phone = models.CharField(max_length=15) 
    

class ResortCompany(Company):
    price_range = models.CharField(max_length=50)  
    profile_picture = models.ImageField(upload_to='ResortLogo', blank=True, null=True)
    phone = models.CharField(max_length=15) 
    

class ServicesCompany(Company):
    types = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='ServiceLogo', blank=True, null=True)
    phone = models.CharField(max_length=15) 
    

class AirCompany(Company):
    phone = models.CharField(max_length=15) 
    price_range = models.CharField(max_length=50)  
    profile_picture = models.ImageField(upload_to='AirLogo', blank=True, null=True)


class BusCompany(Company):
    phone = models.CharField(max_length=15) 
    price_range = models.CharField(max_length=50)  
    profile_picture = models.ImageField(upload_to='BusLogo', blank=True, null=True) 
    

class TrainCompany(Company):
    phone = models.CharField(max_length=15) 
    price_range = models.CharField(max_length=50)  
    profile_picture = models.ImageField(upload_to='TrainLogo', blank=True, null=True)  


    
class LifestyleCompany(Company):
    phone = models.CharField(max_length=15) 
    open_time = models.TimeField(blank=True, null=True) 
    close_time = models.TimeField(blank=True, null=True)  
    profile_picture = models.ImageField(upload_to='LifestyleLogo', blank=True, null=True)   


class ShoppingCompany(Company):
    phone = models.CharField(max_length=15) 
    open_time = models.TimeField(blank=True, null=True)  
    close_time = models.TimeField(blank=True, null=True)  
    profile_picture = models.ImageField(upload_to='ShoppingLogo', blank=True, null=True)


class BabyCareCompany(Company):
    phone = models.CharField(max_length=15) 
    open_time = models.TimeField(blank=True, null=True)  
    close_time = models.TimeField(blank=True, null=True)  
    profile_picture = models.ImageField(upload_to='BabyCareLogo', blank=True, null=True)
    

# Create your models here.
