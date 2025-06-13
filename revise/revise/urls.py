from django.contrib import admin
from django.urls import path
from api.views import StudentApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',StudentApiView.as_view()),
    path('students/<int:pk>/',StudentApiView.as_view()),
]
