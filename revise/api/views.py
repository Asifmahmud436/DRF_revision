from .models import Student
from .serializer import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    stream = io.BytesIO(request.body)
    pythonData = JSONParser().parse(stream)
    
    if request.method == "GET":
        id = pythonData.get('id',None)
        
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student,many=True)
        json_data = JSONRenderer().render(serializer.data)
        
    if request.method == "POST":
        serializer = StudentSerializer(data = pythonData)
        if serializer.is_valid():
            serializer.save()
            response = {"Message":"New student added."}
            json_data = JSONRenderer().render(response)
        else:
            json_data = JSONRenderer().render(serializer.errors)
            
    if request.method == 'PUT':
        id = pythonData.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data = pythonData,partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {"Message":"Student Data Updated!"}
            json_data = JSONRenderer().render(response)
        else:
            json_data = JSONRenderer().render(serializer.errors)

    if request.method == 'DELETE':
        id = pythonData.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        response = {"Message":"Student Deleted"}
        json_data = JSONRenderer().render(response)

    return HttpResponse(json_data,content_type = 'application/json')