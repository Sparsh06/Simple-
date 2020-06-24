from django.contrib import admin

# Register your models here.
from .models import User,ActiviyPeriods

admin.site.register(User)
admin.site.register(ActiviyPeriods)