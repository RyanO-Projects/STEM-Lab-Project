from django.db import models

class Tutor(models.Model):
    day = models.DateField("Tutoring day", help_text="Tutoring day")
    start_time = models.TimeField("Start time", help_text="Start time")
    end_time = models.TimeField("End time", help_text="End time")
    