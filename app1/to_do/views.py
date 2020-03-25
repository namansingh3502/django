from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Task
from django.urls import reverse
import datetime


def home(request):
	latest_task_list = Task.objects.order_by('due_date')[:5]
	template = loader.get_template('to_do/home.html')
	context = {
		'latest_task_list' : latest_task_list
	}
	return HttpResponse(template.render(context, request))

def completed(request):
	latest_task_list = Task.objects.order_by('due_date')[:5]
	template = loader.get_template('to_do/completed.html')
	context = {
		'latest_task_list' : latest_task_list
	}
	return HttpResponse(template.render(context, request))

def newtask(request):
	if request.method == 'POST':
		if request.POST.get('task'):
			task=Task()
			task.task_text=request.POST.get('task')
			task.due_date=datetime.datetime.now()
			task.save()
		return home(request)
	else:
		return home(request)

