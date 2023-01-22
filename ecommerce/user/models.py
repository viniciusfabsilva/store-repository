from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    birth_date = models.DateField()
