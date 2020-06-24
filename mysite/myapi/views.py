from django.shortcuts import render
from rest_framework import viewsets

from .serializer import UserSerializer, ActivitySerializer
from .models import User,ActiviyPeriods

# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class ActivitySet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = ActiviyPeriods.objects.all()