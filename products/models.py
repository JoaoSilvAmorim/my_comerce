from django.db import models

class Product(models.Model):
  description = models.CharField(max_length=50)
  brand = models.CharField(max_length=22)
  amount = models.IntegerField()
  price = models.FloatField()