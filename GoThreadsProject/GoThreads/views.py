from django.shortcuts import render
from .models import Company, CarCompany, Vehicle, HotelCompany, MedicalCompany, Doctor, OnlineCoursesCompany, ResortCompany, ServicesCompany, AirCompany, BusCompany, TrainCompany, LifestyleCompany, ShoppingCompany, BabyCareCompany
from django.template import loader
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

    
def company_list(request):
    companies = Company.objects.all()  # Fetch all Company objects
    return render(request, 'company_list.html', {'companies': companies})

def car_company_list(request):
    car_companies = CarCompany.objects.all()  # Fetch all CarCompany objects
    return render(request, 'car_company_list.html', {'car_companies': car_companies})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()  # Fetch all Vehicle objects
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

def hotel_company_list(request):
    hotel_companies = HotelCompany.objects.all()  # Fetch all HotelCompany objects
    return render(request, 'hotel_company_list.html', {'hotel_companies': hotel_companies})

def medical_company_list(request):
    medical_companies = MedicalCompany.objects.all()  # Fetch all MedicalCompany objects
    return render(request, 'medical_company_list.html', {'medical_companies': medical_companies})

def doctor_list(request):
    doctors = Doctor.objects.all()  # Fetch all Doctor objects
    return render(request, 'doctor_list.html', {'doctors': doctors})

def online_courses_company_list(request):
    online_courses_companies = OnlineCoursesCompany.objects.all()  # Fetch all OnlineCoursesCompany objects
    return render(request, 'online_courses_company_list.html', {'online_courses_companies': online_courses_companies})

def resort_company_list(request):
    resort_companies = ResortCompany.objects.all()  # Fetch all ResortCompany objects
    return render(request, 'resort_company_list.html', {'resort_companies': resort_companies})

def services_company_list(request):
    services_companies = ServicesCompany.objects.all()  # Fetch all ServicesCompany objects
    return render(request, 'services_company_list.html', {'services_companies': services_companies})

def air_company_list(request):
    air_companies = AirCompany.objects.all()  # Fetch all AirCompany objects
    return render(request, 'air_company_list.html', {'air_companies': air_companies})

def bus_company_list(request):
    bus_companies = BusCompany.objects.all()  # Fetch all BusCompany objects
    return render(request, 'bus_company_list.html', {'bus_companies': bus_companies})

def train_company_list(request):
    train_companies = TrainCompany.objects.all()  # Fetch all TrainCompany objects
    return render(request, 'train_company_list.html', {'train_companies': train_companies})

def lifestyle_company_list(request):
    lifestyle_companies = LifestyleCompany.objects.all()  # Fetch all LifestyleCompany objects
    return render(request, 'lifestyle_company_list.html', {'lifestyle_companies': lifestyle_companies})

def shopping_company_list(request):
    shopping_companies = ShoppingCompany.objects.all()  # Fetch all ShoppingCompany objects
    return render(request, 'shopping_company_list.html', {'shopping_companies': shopping_companies})

def baby_care_company_list(request):
    baby_care_companies = BabyCareCompany.objects.all()  # Fetch all BabyCareCompany objects
    return render(request, 'baby_care_company_list.html', {'baby_care_companies': baby_care_companies})
