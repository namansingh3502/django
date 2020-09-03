from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,get_object_or_404
from .models import Creator,Participant
from .forms import UserPass,NewUser
from django.urls import reverse
import secrets
import string
import json

def signin( request ):

	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)

		form = UserPass( body )

		if form.is_valid():


			user = body.get('username')
			password = body.get('password')
			user_type = body.get('user_type')

			if user_type == "participant" and Participant.objects.filter( username = user ).exists():
				cred = Participant.objects.filter( username = user )

			elif user_type == "creator" and Creator.objects.filter( username = user ).exists():
				cred = Creator.objects.filter( username = user )
			
			else:
				return JsonResponse({'status':False}, status=404 )

			if password == cred[0].password:
				token = cred[0].token
				pk = cred[0].pk
				return JsonResponse({'status':True,'token':token,'pk':pk}, status=200 )

			else:
				return JsonResponse({'status':False}, status=404 )

		else:
			return JsonResponse({'status':False}, status=404 )
	
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
			user_type = body.get('user_type')
			
			if user_type == "participant":
				if Participant.objects.filter( username = user ).exists():
					return JsonResponse({'status':'false'}, status=404 )
				else:
					cred = Participant()
			else:
				if Cred.objects.filter( username = user ).exists():
					return JsonResponse({'status':'false'}, status=404 )
				else:
					cred = Creator()

			alphabet = string.ascii_letters + string.digits
			token = ''.join(secrets.choice(alphabet) for i in range( 32 ))

			cred.name = body.get('name')
			cred.username = user
			cred.password = body.get('password')
			cred.token = token
			cred.save()

			return JsonResponse({'status':True}, status=200 )

		else:
			form = NewUser()
			return JsonResponse({'status':'false'}, status=404 )

	else:
		form = NewUser()
		return render(request, 'login/signup.html', {'form': form})




	
