from django.db import models

# Create your models here.

class user(models.Model):
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 6)