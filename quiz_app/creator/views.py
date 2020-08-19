from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

def dashboard( request ):
	
	return HttpResponse(" hello ")