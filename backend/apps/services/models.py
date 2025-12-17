from django.db import models
from apps.business.models import Business

# Create your models here.
class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
