from django.db import models
from django.utils import timezone
import datetime

class Task(models.Model):
	task_text = models.CharField(max_length=20)
	due_date = models.DateTimeField('due date')
	status = models.IntegerField(default=0)