from django.contrib import admin
from .models import Exam,Login,StudentRegistration


# Register your models here
admin.site.register(StudentRegistration)
admin.site.register(Exam)
admin.site.register(Login)
