from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from portals.GM2 import GenericMethodsMixin
from rest_framework import status
from rest_framework.views import APIView
from .serializers import * 
from .models import * 
from django.db import transaction

class CompanyAPI(GenericMethodsMixin,APIView):
    model = Company
    serializer_class = CompanySerializer
    lookup_field = "id"

class ServiceAPI(GenericMethodsMixin,APIView):
    model = Service
    serializer_class = ServiceSerializer
    lookup_field = "id"


    def post(self,request,*args,**kwargs):
        with transaction.atomic():
            print("--------------------------------------",request.data)

            data = request.data
            serializer = ServiceSerializer(data=data)
            if serializer.is_valid() :
                service = serializer.save()
                #owner
                
                #employee
                # opening hours 
                # price

class OwnerAPI(GenericMethodsMixin,APIView):
    model = Owner
    serializer_class = OwnerSerializer
    lookup_field = "id"

class EmployeeAPI(GenericMethodsMixin,APIView):
    model = Employee
    serializer_class = EmployeeSerializer
    lookup_field = "id"

class OpeningHoursAPI(GenericMethodsMixin,APIView):
    model = OpeningHours
    serializer_class = OHSerializer
    lookup_field = "id"

class PriceAPI(GenericMethodsMixin,APIView):
    model = Price
    serializer_class = PriceSerializer
    lookup_field = "id"