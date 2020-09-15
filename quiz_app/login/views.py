from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,get_object_or_404
from .forms import UserPass,NewUser
from django.urls import reverse
from .models import User
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

			if User.objects.filter( username = user ).exists():
				cred = User.objects.filter( username = user )
			
			else:
				return JsonResponse({'status':False}, status=404 )

			if password == cred[0].password and user_type == cred[0].usertype:
				token = cred[0].token
				return JsonResponse({'status':True,'token':token}, status=200 )

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

			user_name = body.get('username')
			user_type = body.get('user_type')
			
			if User.objects.filter( username = user_name ).exists():
				return JsonResponse({'status':False}, status=404 )

			else:
				cred = User()

			alphabet = string.ascii_letters + string.digits
			token = ''.join(secrets.choice(alphabet) for i in range( 64 ))

			cred.name = body.get('name')
			cred.username = user_name
			cred.password = body.get('password')
			cred.token = token
			cred.usertype = user_type
			cred.save()

			return JsonResponse({'status':True}, status=200 )

		else:
			form = NewUser()
			return JsonResponse({'status':False}, status=404 )

	else:
		form = NewUser()
		return render(request, 'login/signup.html', {'form': form})

