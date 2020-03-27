from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Task
from django.urls import reverse
import datetime


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
	print(request.POST.get('task'))
	if request.method == 'POST':
		if request.POST.get('task'):
			task=Task()
			task.task_text=request.POST.get('task')
			task.due_date=datetime.datetime.now()
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
			task.due_date=datetime.datetime.now()
			task.save()
			return HttpResponseRedirect(reverse('todo:completed'))
		else:
			task.status += 1
			task.due_date=datetime.datetime.now()
			task.save()
		return HttpResponseRedirect(reverse('todo:home'))


#def vote(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'polls/detail.html', {
#            'question': question,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))