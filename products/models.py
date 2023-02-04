import uuid
from django.db import models
from user.models import User

class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=240)
  description = models.CharField(max_length=240, null=True, blank=True)
  brand = models.CharField(max_length=22)
  amount = models.IntegerField()
  price = models.FloatField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)