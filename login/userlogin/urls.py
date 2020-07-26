from django.urls import path
from . import views

app_name = 'userlogin'

urlpatterns = [
	
	#path( '', views.home, name = 'home' ),
	
	path( '', views.signin, name = 'signin' ),
	
	path( 'signup/', views.signup, name = 'signup' )
]