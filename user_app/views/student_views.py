from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from ..serializers import *
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from ..serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
