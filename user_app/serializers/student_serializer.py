from rest_framework import serializers
from ..models import *
from .user_serializer import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user',  'descriptions']
