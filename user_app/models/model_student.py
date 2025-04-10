# from .model_teacher import *
#
# class Student(BaseModel):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     group = models.ManyToManyField(GroupStudent, related_name='get_group')
#     descriptions = models.CharField(max_length=500, null=True, blank=True)
#
#     def __str__(self):
#         return self.user.phone
#