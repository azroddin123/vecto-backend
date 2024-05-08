from django.urls import path
from .views import *

urlpatterns = [

    path('company',CompanyAPI.as_view()),
    path('company/<str:pk>', CompanyAPI.as_view()),
   
    path('service',ServiceAPI.as_view()),
    path('service/<str:pk>', ServiceAPI.as_view()),

    path('employee',EmployeeAPI.as_view()),
    path('employee/<str:pk>', EmployeeAPI.as_view()),

    path('owner',OwnerAPI.as_view()),
    path('owner/<str:pk>', OwnerAPI.as_view()),

    path('opening-hours',ServiceAPI.as_view()),
    path('opening-hours/<str:pk>', ServiceAPI.as_view()),

    path('price',ServiceAPI.as_view()),
    path('price/<str:pk>', ServiceAPI.as_view()),

]