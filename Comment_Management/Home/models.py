from re import M
from django.db import models

# Create your models here.
class User(models.Model):
    Comment=models.CharField(max_length=500)