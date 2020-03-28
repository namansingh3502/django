from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Task
from django.urls import reverse
from datetime import datetime
from django.utils.dateparse import parse_datetime
def home(request):
	latest_task_list = Task.objects.order_by('due_date')
	template = loader.get_template('to_do/home.html')
	context = {
		'latest_task_list' : latest_task_list
	}
	return HttpResponse(template.render(context, request))

def completed(request):
	latest_task_list = Task.objects.order_by('due_date')
	template = loader.get_template('to_do/completed.html')
	context = {
		'latest_task_list' : latest_task_list
	}
	return HttpResponse(template.render(context, request))

def newtask(request):
	print(request.POST.get('task') + " " + request.POST.get('date')+" "+ request.POST.get('time'))
	if request.method == 'POST':
		if request.POST.get('task') and request.POST.get('date'):
			date=request.POST.get('date')
			time=request.POST.get('time')
			date_time=str(date)+" "+str(time)
			task=Task()
			task.task_text=request.POST.get('task')
			task.due_date=datetime.strptime(date_time, "%Y-%m-%d %H:%M")
			task.save()
		return HttpResponseRedirect(reverse('todo:home'))
	else:
		return HttpResponseRedirect(reverse('todo:home'))

def change(request,task_id):
	if task_id:	
		task=get_object_or_404(Task, pk=task_id)
		print(str(task.status) + " " + str(task_id))
		if task.status==1:
			task.status -= 1
			task.save()
			return HttpResponseRedirect(reverse('todo:completed'))
		else:
			task.status += 1
			task.save()
		return HttpResponseRedirect(reverse('todo:home'))
