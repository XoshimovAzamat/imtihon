from django.contrib import admin
from .models import *

admin.site.register([Teacher, Course, Departments, User, GroupStudent, Student])
