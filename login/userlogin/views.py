from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Userdata
from .forms import UserPass,NewUser

def signin( request ):

	if request.method == 'POST':
		form = UserPass( request.POST )

		if form.is_valid():

			user = request.POST.get('username')
			user_pass = request.POST.get('password')

			if Userdata.objects.filter( username = user ).exists():

				cred = Userdata.objects.filter( username = user )

				if cred[0].password == user_pass:
					return HttpResponse( "Succesfully logged In " )
			
			
			form = UserPass()
			return render(request, 'userlogin/signin2.html', {'form': form})
	
	else:
		form = UserPass()
		return render(request, 'userlogin/signin.html', {'form': form})


def signup( request ):

	if request.method == 'POST':
		form = NewUser( request.POST )
		
		if form.is_valid():

			user = request.POST.get('username')

			if Userdata.objects.filter( username = user ).exists():
				return render(request, 'userlogin/signup2.html', {'form': form})

			cred=Userdata()

			cred.name = request.POST.get('name')
			cred.username = request.POST.get('username')
			cred.password = request.POST.get('password')
			cred.save()

			return HttpResponseRedirect(reverse('userlogin:signin'))

	else:
		form = NewUser()
		return render(request, 'userlogin/signup.html', {'form': form})

