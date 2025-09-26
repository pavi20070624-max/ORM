from django.contrib import admin
from django.db import models
class CAR_INVENTORY (models.Model):
    model_name=models.CharField(max_length=15)
    year_of_manufacture=models.IntegerField()
    price=models.IntegerField()
    color=models.CharField(max_length=15)
    mileage=models.IntegerField()
    number_of_seats=models.IntegerField()

class CAR_INVENTORYAdmin(admin.ModelAdmin):
    list_display=('model_name','year_of_manufacture','price','color','mileage','number_of_seats')
# Create your models here.
