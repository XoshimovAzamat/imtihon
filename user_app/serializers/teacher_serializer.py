from rest_framework import serializers
from ..models import Teacher, User, Course, Departments
from .user_serializer import *


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    departments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Departments.objects.all()
    )
    course = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all()
    )

    class Meta:
        model = Teacher
        fields = ['id','user', 'departments', 'course', 'descriptions']

# from rest_framework import serializers
# from user_app.models import Teacher
# from rest_framework import serializers
# from .models import Teacher, Departments, Course
# from django.contrib.auth.models import User
#
# from .user_serializer import UserSerializer
#
#
# # class TeacherSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Teacher
# #         fields = ["id", "user", "departments","course", "descriptions"]
# #
# class TeacherUserSerializer(serializers.ModelSerializer):
#     is_active = serializers.BooleanField(read_only=True)
#     is_teacher = serializers.BooleanField(read_only=True)
#     is_admin = serializers.BooleanField(read_only=True)
#     is_student = serializers.BooleanField(read_only=True)
#     is_staff = serializers.BooleanField(read_only=True)
#
#
# class Meta:
#     model = User
#     fields = (
#         'id', 'phone', 'password', "full_name", 'is_active', 'is_staff', "is_teacher", 'is_admin', 'is_student')
#
#
# class TeacherSerializer(serializers.Serializer):
#     user = UserSerializer()
#     teacher = TeacherSerializer()
