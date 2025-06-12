from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializer import StudentSerializer

def student_detail(request,pk):
    student = Student.objects.get(id=pk)
    serialize = StudentSerializer(student)
    return JsonResponse(serialize.data)

def all_student(request):
    student = Student.objects.all()
    serialize = StudentSerializer(student,many=True)
    return JsonResponse(serialize.data,safe=False)
