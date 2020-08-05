from django.db import models

# Create your models here.

class Userdata( models.Model ):
	name = models.CharField( max_length = 10 )
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 10)
