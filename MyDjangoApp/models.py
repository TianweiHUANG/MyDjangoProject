from django.db import models

# Create your models here.

class Tabs(models.Model):
    value_a = models.CharField(max_length=10)
    value_b = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
