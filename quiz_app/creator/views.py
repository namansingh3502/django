from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,get_object_or_404
from login.models import User
from django.urls import reverse
import secrets
import string
import json

def user_verification( request, username, token ):

	return HttpResponse ( "hello  " + username )

