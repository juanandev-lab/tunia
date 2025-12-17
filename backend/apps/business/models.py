from django.db import models
from apps.accounts.models import User

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="businesses")
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
