from django.db import models


# Create your models here.
class Remember(models.Model):
    title = models.CharField(max_length=120)
    start_day = models.DateField()
    end_day = models.DateField()
    time = models.TimeField()
