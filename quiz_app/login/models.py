from django.db import models

# Create your models here.

class User ( models.Model ):
	name = models.CharField( max_length = 128 )
	username = models.CharField( max_length = 128 )
	password = models.CharField( max_length = 128 )
	token = models.CharField( max_length = 128 )
	usertype = models.CharField( max_length = 10 )


