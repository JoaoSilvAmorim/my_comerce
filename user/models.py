from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  cpf = models.CharField(max_length=16)
  idade = models.IntegerField(blank=True, null=True)

