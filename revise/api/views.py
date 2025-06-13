from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin

class LCstudentApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.post(request,*args,**kwargs)
    
class RUDstudentApiView(GenericAPIView,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
