import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)

class User(AbstractUser):
  TYPE_USER = (
        ("C", "Cliente"),
        ("S", "Sistema")
  )
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  cpf = models.CharField(max_length=16)
  idade = models.IntegerField(blank=True, null=True)
  type = models.CharField(max_length=1, choices=TYPE_USER, blank=False, null=False)
  client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
