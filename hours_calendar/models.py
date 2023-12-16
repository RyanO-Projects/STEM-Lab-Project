from django.db import models

class Event(models.Model):
    tutor = models.CharField(max_length=200)
    subjects = models.CharField(max_length=500, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()