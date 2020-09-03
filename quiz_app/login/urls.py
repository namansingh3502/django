from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
	
	path( '', views.signin, name = 'signin' ),
		
	path( 'new_user/', views.signup, name = 'signup' ),
	
	path( 'recpass/', views.signin, name = "recpass")
	
]