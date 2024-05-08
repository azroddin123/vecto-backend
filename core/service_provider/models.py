from django.db import models
from accounts.models import User
# Create your models here.
from portals.models import BaseModel
from portals.choices import PriceChoices
class Company(BaseModel):
    user             = models.ForeignKey(User,on_delete=models.CASCADE)
    name             = models.CharField(max_length=256)
    contact_no       = models.CharField(max_length=256)
    company_logo     = models.ImageField()
    description      =  models.TextField()
    country          = models.CharField(max_length=256)
    state            = models.CharField(max_length=256)
    city             = models.CharField(max_length=256)
    zip_code         = models.CharField(max_length=256)
    street_address   = models.CharField(max_length=256)
    package          = models.CharField(max_length=256)

class Service(BaseModel):
    name           = models.CharField(max_length=256)
    description    = models.CharField(max_length=256)
    category       = models.CharField(max_length=256)
    buffer_time    = models.IntegerField(default=30)

class Owner(BaseModel):
    service       = models.OneToOneField(Service,on_delete=models.CASCADE)
    name          = models.CharField(max_length=256)
    mobile_number = models.CharField(max_length=256)
    profile_pic   = models.ImageField()
    bio           = models.CharField(max_length=256)

class Employee(BaseModel):
    service        = models.ForeignKey(Service,on_delete=models.CASCADE)
    name           = models.CharField(max_length=256)
    mobile_number  = models.CharField(max_length=256)
    profile_pic    = models.ImageField()
    bio            = models.CharField(max_length=256)

class OpeningHours(BaseModel):
    service        = models.ForeignKey(Service,on_delete=models.CASCADE)
    day            = models.CharField(max_length=20)
    opening_time   = models.TimeField(default="09:00")
    closing_time   = models.TimeField(default="17:00")

class Price(BaseModel):
    service          = models.ForeignKey(Service,on_delete=models.CASCADE)
    price_per_hour    = models.DecimalField(max_digits=10, decimal_places=2)
    employee_type     = models.CharField(PriceChoices,max_length=256,default=PriceChoices.BEGINNER)
   


