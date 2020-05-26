import datetime
from django.db import models
from django.utils import timezone


class User(models.Model):
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 10)

class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task_text = models.CharField(max_length=20)
	due_date = models.DateTimeField('due date')
	status = models.IntegerField(default=0)
