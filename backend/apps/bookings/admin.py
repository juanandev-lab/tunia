from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("business", "service", "customer_name", 
                    "customer_phone", "start_time", "end_time", 
                    "status", "created_at")