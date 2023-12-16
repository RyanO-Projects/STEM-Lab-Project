from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name
    

class TimeSlot(models.Model):
    DAY_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
    ]
    TIME_CHOICES = [
        ('8:00-9:00 AM', '8:00-9:00 AM'),
        ('9:00-10:00 AM', '9:00-10:00 AM'),
        ('10:00-11:00 AM', '10:00-11:00 AM'),
        ('11:00-12:00 PM', '11:00-12:00 PM'),
        ('12:00-1:00 PM', '12:00-1:00 PM'),
        ('1:00-2:00 PM', '1:00-2:00 PM'),
        ('2:00-3:00 PM', '2:00-3:00 PM'),
        ('3:00-4:00 PM', '3:00-4:00 PM'),
        ('4:00-5:00 PM', '4:00-5:00 PM'),
        ('5:00-6:00 PM', '5:00-6:00 PM'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES, default="Monday")
    time = models.CharField(max_length=50, choices=TIME_CHOICES, default="9:00-10:00 AM")

    def __str__(self):
        return f"{self.day} - {self.time}"
    

class Tutor(models.Model):
    name = models.CharField(max_length=100, default="")
    tutoring_times = models.ManyToManyField(TimeSlot)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name