from django.db import models

class TutorShift(models.Model):
    day = models.DateField('Tutoring day', help_text='Tutoring day')
    start_time = models.TimeField('Start time', help_text='Start time')
    end_time = models.TimeField('End time', help_text='End time')
    notes = models.TextField('Textual Notes', help_text='Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = 'Scheduling'
        verbose_name_plural = 'Scheduling'
