from django.db import models
from apps.business.models import Business
from apps.services.models import Service

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pendiente"),
        ("confirmed", "Confirmado"),
        ("cancelled", "Cancelado"),
        ("completed", "Completado"),
    )

    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

