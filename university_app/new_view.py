from rest_framework.generics import ListAPIView
from .models import *
from rest_framework import viewsets
from .modelserializer import *


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer