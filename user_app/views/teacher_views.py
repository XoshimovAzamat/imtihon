from rest_framework.response import Response
from rest_framework.views import APIView
from user_app.models import *
from ..serializers import *
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from ..serializers import TeacherSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet


class TeacherApi(APIView):
    def get(self, request):
        data = {"success": True}
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        data['teacher'] = serializer.data
        return Response(data=data)

    @swagger_auto_schema(request_body=TeacherPostSerializer)
    def post(self, request):
        data = {"success": True}
        user = request.data['user']
        teacher = request.data['teacher']
        phone_number = user['phone_number']
        user_serializer = UserSerializer(data=user)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.is_teacher = True
            user_serializer.is_active = True
            user_serializer.password = (
                make_password(user_serializer.validated_data.get('password'))
            )
            user = user_serializer.save()
            user_id = User.objects.filter(phone_number=phone_number).values('id')[0]['id']
            teacher['user'] = user_id
            teacher_serializer = TeacherSerializer(data=teacher)
            if teacher_serializer.is_valid(raise_exception=True):
                teacher_serializer.save()
                data['user'] = user_serializer.data
                data['teacher'] = teacher_serializer.data
                return Response(data=data)
            return Response(data=teacher_serializer.errors)
        return Response(data=user_serializer.errors)


# class TeacherViewSet(ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherPostSerializer
