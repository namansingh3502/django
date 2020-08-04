from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Userdata
from .forms import UserPass

def signin( request ):

	if request.method == 'POST':
		form = UserPass(request.POST)
		print(request.POST)
		
		if form.is_valid():
			
			return HttpResponseRedirect(reverse('userlogin:signin'))

	else:
		form = UserPass()

	return render(request, 'userlogin/signin.html', {'form': form})
	#return render( request, 'userlogin/signin.html' )

def signup( request ):

	if request.method == 'POST':
		form = UserPass(request.POST)
		
		if form.is_valid():
			return HttpResponseRedirect('userlogin:home')

	else:
		form = UserPass()

	return render(request, 'signup.html', {'form': form})
	#return render( request, 'userlogin/signup.html' )

