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

	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)

	user_type = body.get('user_type')

	if ( user_type == "participant" or user_type == "creator" ) and request.method == 'POST':
		
		form = UserPass()
		return render( request, 'login/signin.html', { 'form': form } )
		
		form = UserPass( body )

		if form.is_valid():

			user = body.get('username')
			password = body.get('password')

			if user_type == "participant":
				pk = get_object_or_404( Participant, username = user ).pk

			else:
				pk = get_object_or_404( Creator, username = user ).pk

			if (  )





def signup( request ):

	if request.method == 'POST':
		body_unicode = request.decode('utf-8')
		body = json.loads(body_unicode)

		form = UserPass( body )

		if form.is_valid():

			username = body.get('username')

			if Participant.objects.filter( username = user ).exist() and Creator.objects.filter( username = user ).exist():
				message = "Username already exist"
				return JsonResponse({'status':'false','message':message}, status=404 )

			user_type = body.get('user_type')
			
			if user_type == "participant":
				cred = Participant()
			else:
				cred = Creator()

			alphabet = string.ascii_letters + string.digits
			token = ''.join(secrets.choice(alphabet) for i in range( 16 ))

			cred.name = body.get('name')
			cred.username = username
			cred.password = body.get('password')
			cred.token = token
			cred.save()

			return HttpResponseRedirect(reverse('login:home'))

		else:
			form = NewUser()
			message = "Ooops! Some error occured. Check username/password"
			return JsonResponse({'status':'false','message':message}, status=500 )

	else:
		form = NewUser()
			return render(request, 'login/signup.html', {'form': form})




	