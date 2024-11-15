
from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSEt, EmployeeViewSEt
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSEt)
router.register(r'employees', EmployeeViewSEt)

urlpatterns = [
    path('', include(router.urls))
 
]
