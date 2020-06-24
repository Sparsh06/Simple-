from django.db import models
from django.utils import timezone
import datetime
import uuid
# Create your models here.


class User(models.Model):
    id = models.CharField(primary_key=True,unique=True,default=uuid.uuid4,max_length=10)
    real_name=models.CharField(max_length=50)
    tz = timezone.now()
    activity_periods = models.ForeignKey('ActiviyPeriods',on_delete=models.CASCADE)

    def __str__(self):

        return '%s %s %s %s'%(self.id, self.real_name, self.tz,self.activity_periods)
class ActiviyPeriods(models.Model):
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()

    def __str__(self):
        return '%s %s'%(self.start_time, self.end_time)

