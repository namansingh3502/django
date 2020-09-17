from django.urls import path
from .import views

app_name = 'creator'

urlpatterns = [
	
	path( '<str:username>/', views.dashboard, name = "dashboard" ),

]