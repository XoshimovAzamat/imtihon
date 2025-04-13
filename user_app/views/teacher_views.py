from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Teacher
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

    @swagger_auto_schema(request_body=TeacherSerializer)
    def post(self, request):
        data = {"success": True}
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data['data'] = serializer.data
            return Response(data=data)
        return Response(serializer.errors)


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

