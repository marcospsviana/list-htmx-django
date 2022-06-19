from django.contrib import admin
from tasklist.radio.models import Radio, City
# Register your models here.

@admin.register(Radio)
class RadioAdmin(admin.ModelAdmin):
    fields = ('name', 'dial', 'cities')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ('name',)