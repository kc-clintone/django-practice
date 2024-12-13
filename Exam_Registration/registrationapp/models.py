from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.template.defaulttags import now

class Login(models.Model):
  username=models.CharField(max_length=100)
  password=models.CharField(max_length=100)

  def __str__(self):
      return f'{self.username}'

class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title


#class StudentRegistration(models.Model):
#    name = models.CharField(max_length=100)
#    email = models.EmailField()
#    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="registrations")

#    def __str__(self):
#        return f"{self.name} - {self.exam.title}"


class StudentRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="registrations")

    class Meta:
        unique_together = ('user', 'exam')

    def __str__(self):
        return f"{self.user.username} - {self.exam.title}"
