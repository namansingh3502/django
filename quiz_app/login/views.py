from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Creator,Participant
from .forms import UserPass,NewUser
import json

def home( request ):
	return render( request, 'login/home.html') 

def signin( request ):

	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		print(body)

		if form.is_valid():

			user = request.POST.get('username')
			user_pass = request.POST.get('password')

			if user_type == "participant":
				cred = Participant.objects.filter( username = user )

			else: cred = Creator.objects.filter( username = user )

			if cred :
				if cred[0].password == user_pass:
					return HttpResponse( "Succesfully logged In " )
			else:
				form = UserPass()
				return render( request, 'login/signin2.html', { 'form': form } )

		else:
			form = UserPass()
			return render( request, 'login/signin.html', { 'form': form } )

		return JsonResponse( data, safe = False )

	else:

		form = UserPass()
		return render( request, 'login/signin.html', { 'form': form } )

def signup( request ):

	if request.method == 'POST':
		print(request.POST)
		form = NewUser( request.POST )

		if form.is_valid():

			user = request.POST.get('username')
			u_type = request.POST.get('user_type')

			status = 1;

			if u_type == "participant" and Participant.objects.filter( username = user ).exists():
				status = 0
				return render(request, 'login/signup2.html', {'form': form})

			if u_type == "Creator" and Creator.objects.filter( username = user ).exists():
				status = 0
				return render(request, 'login/signup2.html', {'form': form})

			if status == 1:
				if u_type == "participant":
					cred = Participant()
				else:
					cred = Creator()


				cred.name = request.POST.get('name')
				cred.username = request.POST.get('username')
				cred.password = request.POST.get('password')
				cred.save()
				return HttpResponseRedirect(reverse('login:home' ))

		else:
			form = NewUser()
			return render(request, 'login/signup.html', {'form': form})
	else: 
		form = NewUser()
		return render(request, 'login/signup.html', {'form': form} )


	