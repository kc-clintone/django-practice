from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=30)
    location = models.CharField
    description = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='event_posters/')
    registration_link = models.URLField()
    registered_users = models.ManyToManyField(User, related_name='registered_events', blank=True)

    def __str__(self):
        return self.name

class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
