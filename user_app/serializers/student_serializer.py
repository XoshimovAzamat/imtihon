from rest_framework import serializers
from ..models import *
from .user_serializer import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user',  'group','descriptions']


class StudentUserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'password', 'is_active', 'is_staff', "is_teacher", 'is_admin',
            'is_student')


class StudentPostSerializer(serializers.Serializer):
    user = StudentUserSerializer()
    student = StudentSerializer()
