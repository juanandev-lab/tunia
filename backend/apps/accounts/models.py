from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """
    Usuario base del sistema.
    En la MVP representa a un autónomo propietario de su negocio.
    """
    email = models.EmailField(unique=True)