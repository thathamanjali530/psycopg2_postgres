from django.db import models

# Create your models here.
class school(models.Model):
    Scname=models.CharField(max_length=100)
    Scloc=models.CharField(max_length=100)
