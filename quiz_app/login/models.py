from django.db import models

# Create your models here.

class Creator ( models.Model ):
	name = models.CharField( max_length = 40 )
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 10)

class Participant ( models.Model ):
	name = models.CharField( max_length = 40 )
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 10)