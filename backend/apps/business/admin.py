from django.contrib import admin
from .models import Business

# Register your models here.
@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "phone", "address", "is_active", "created_at")