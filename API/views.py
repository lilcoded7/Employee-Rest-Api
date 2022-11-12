from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from .serializers import RegisterSerializer, EmployeeRegisterSerializer
from .utils import Util
from .models import MyUser, EmployeeRecord
from django.http import Http404
from rest_framework import permissions


# super user api view 
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            user_data = serializer.data
            user = MyUser.objects.get(email=user_data['email'])

            email_body = ' Congratulation, Your Account is successfully Registed'

            data = {
                'subject'    : 'Tropiteq',
                'email_body' : email_body,
                'to'         : user.email      
            }
            Util.send_email(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# employee api view 
class EmployeeRegister(APIView):

    def get(self, request):
        user = EmployeeRecord.objects.all()
        serializer = EmployeeRegisterSerializer(user, many=True)
        return Response(serializer.data)
        

    def post(self, request):
        
        # id = EmployeeRecord.IDGenetator(request.data['first_name', 'last_name'])
            # saveID = EmployessRecord.objects.create_user(userID=id)
            # user.save 

        serializer = EmployeeRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# employee api update view
class EmployeeDetails(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return EmployeeRecord.objects.get(pk=pk)
        except Employee.Does.NotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeRegisterSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeRegisterSerializer(employee, data=reaquest.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.deleata()
        return Response(status=status.HTTP_204_NO_CONTENT)
