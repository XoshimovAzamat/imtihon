from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Teacher
from ..serializers import *
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from ..serializers import TeacherSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet


class StudentApi(APIView):
    def get(self, request):
        data = {"success": True}
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        data['student'] = serializer.data
        return Response(data=data)

    @swagger_auto_schema(request_body=StudentPostSerializer)
    def post(self, request):
        data = {"success": True}
        user = request.data['user']
        student = request.data['student']
        phone_number = user['phone_number']
        user['is_student']=True
        user['is_active']=True
        user_serializer = UserSerializer(data=user)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.password = (
                make_password(user_serializer.validated_data.get('password'))
            )
            user = user_serializer.save()
            user_id = User.objects.filter(phone_number=phone_number).values('id')[0]['id']
            student['user'] = user_id
            student_serializer = StudentSerializer(data=student)
            if student_serializer.is_valid(raise_exception=True):
                student_serializer.save()
                data['user'] = user_serializer.data
                data['student'] = student_serializer.data
                return Response(data=data)
            return Response(data=student_serializer.errors)
        return Response(data=user_serializer.errors)


# class TeacherViewSet(ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherPostSerializer
