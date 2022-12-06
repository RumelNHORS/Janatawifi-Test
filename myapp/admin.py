from django.contrib import admin
from . models import Customer, JsonModel

@admin.register(Customer, JsonModel)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'trade_code', 'volume']

class Json_Model_Admin(admin.ModelAdmin):
    list_display = ['id', 'date', 'trade_code', 'volume']