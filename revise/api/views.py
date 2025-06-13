from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView

class StudentApiView(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serialzier = StudentSerializer(student)
            return Response(serialzier.data)
        student = Student.objects.all()
        serialzier = StudentSerializer(student,many=True)
        return Response(serialzier.data)
    
    def post(self, request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'data created!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk,format=None):
        id = pk
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"details updated!"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk, format=None):
        id = pk
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"partially details updated!"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        id = pk
        student = Student.objects.get(id = id)
        student.delete()
        return Response({"message":"Student deleted!"},status=status.HTTP_200_OK)
        

