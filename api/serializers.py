from rest_framework import serializers
from api.models import Company, Employee
# create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"


class EmployeeSErializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model= Employee
        fields = "__all__"
