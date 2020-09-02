from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,get_object_or_404
from .models import Creator,Participant
from .forms import UserPass,NewUser
from django.urls import reverse
import secrets
import string
import json

def home( request ):
	return render( request, 'login/home.html') 

def signin( request ):

	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		
		form = UserPass( body )

		if form.is_valid():

			user = body.get('username')
			password = body.get('password')
			user_type = body.get('user_type')


			if user_type == "participant":
				cred = get_object_or_404( Participant, username = user )

			else:
				cred = get_object_or_404( Creator, username = user )

			if password == cred.password:
				token = cred.token
				return JsonResponse({'token':token}, status=200 )

			else:
				return JsonResponse({'status':'false'}, status=404 )

		else:
			return JsonResponse({'status':'false'}, status=404 )

	else:
		form = UserPass()
		return render( request, 'login/signin.html', { 'form': form } )

def signup( request ):

	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		
		form = NewUser( body )

		if form.is_valid():

			user = body.get('username')

			if Participant.objects.filter( username = user ).exists() or Creator.objects.filter( username = user ).exists():
				message = "Username already exist"
				return JsonResponse({'status':'false','message':message}, status=404 )

			user_type = body.get('user_type')
			
			if user_type == "participant":
				cred = Participant()
			else:
				cred = Creator()

			alphabet = string.ascii_letters + string.digits
			token = ''.join(secrets.choice(alphabet) for i in range( 32 ))

			cred.name = body.get('name')
			cred.username = user
			cred.password = body.get('password')
			cred.token = token
			cred.save()

			return JsonResponse({'status':'false'}, status=200 )

		else:
			form = NewUser()
			message = "Ooops! Some error occured. Check username/password"
			return JsonResponse({'status':'false','message':message}, status=500 )

	else:
		form = NewUser()
		return render(request, 'login/signup.html', {'form': form})




	