from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import User
from django.urls import reverse
from .models import user


def login(request):

	username = User.objects.order_by('due_date')
	password = User.objects
	template = loader.get_template('to_do/home.html')
	context = {
		'latest_task_list' : latest_task_list
	}
	return HttpResponse(template.render(context, request))
    return HttpResponse("Login page")