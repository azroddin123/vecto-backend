from rest_framework.serializers import ModelSerializer
from .models import *


class CompanySerializer(ModelSerializer):
    class Meta :
        model = Company
        fields = "__all__"

class ServiceSerializer(ModelSerializer):
    class Meta :
        model = Service
        fields = "__all__"

class OwnerSerializer(ModelSerializer):
    class Meta :
        model = Owner
        fields = "__all__"

class EmployeeSerializer(ModelSerializer):
    class Meta :
        model = Employee
        fields = "__all__"

class OHSerializer(ModelSerializer):
    class Meta :
        model = OpeningHours
        fields = "__all__"


class PriceSerializer(ModelSerializer):
    class Meta :
        model = Price
        fields = "__all__"
        