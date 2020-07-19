from django.db import models

# Create your models here.
class user_info(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=50)