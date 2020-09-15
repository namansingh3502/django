from django.urls import path
from .import views

app_name = 'creator'

urlpatterns = [
	
	path( 'login/<str:username>/<str:token>/', views.user_verification, name = "user_verification" ),
	#path( '<str:username>/', views.dashboard, name = "dashboard" )

]