from django.db import models

# Create your models here.

class Creator ( models.Model ):
	name = models.CharField( max_length = 40 )
	username = models.CharField( max_length = 128 )
	password = models.CharField( max_length = 128 )
	#token = models.CharField( max_length = 30 )


class Participant ( models.Model ):
	name = models.CharField( max_length = 40 )
	username = models.CharField( max_length = 10 )
	password = models.CharField( max_length = 10 )
	#token = models.CharField( max_length = 30 )