from ast import Or
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display= ['name','price','image']


@admin.register(Order)
class PizzaAdmin(admin.ModelAdmin):
    list_display= ['pizza','user','order_id','amount','status','date']