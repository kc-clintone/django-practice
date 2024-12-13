from django.db import models

# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField
    phone = models.CharField(max_length=20)
    age_group = models.CharField(max_length=10)
    description = models.CharField(max_length=100) 
