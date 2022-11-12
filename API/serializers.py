from rest_framework import serializers
from .models import MyUser, EmployeeRecord
import random



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'phone']


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = EmployeeRecord
        fields = ['first_name', 'last_name', 'email',  'developer_role', 'programming_language']