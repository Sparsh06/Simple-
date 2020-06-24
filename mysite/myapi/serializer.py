# serializers.py
from rest_framework import serializers

from .models import User,ActiviyPeriods

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','real_name','tz','activity_periods']

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActiviyPeriods
        fields = ['start_time','end_time']        