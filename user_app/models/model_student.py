from .model_teacher import *

from ..models import *


class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ManyToManyField(GroupStudent, related_name="get_student")
    course = models.ManyToManyField(Course, related_name="get_student")
    is_line = models.BooleanField(default=False)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.user.phone_number


class Parents(BaseModel):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    ful_name = models.CharField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.ful_name
