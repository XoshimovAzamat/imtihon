from os.path import basename

from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'teacher-crud', TeacherViewSet, basename='teacher')
urlpatterns = [
    path('teacher_post/', TeacherApi.as_view()),
    path('', include(router.urls)),
    path('users/', UserApi.as_view(), name='user-list'),
    path('student_crud/', StudentCrudApi.as_view(), name='student-crud'),
    path('user/', UserStudentCreateApi.as_view(), name='user-crud'),
]
