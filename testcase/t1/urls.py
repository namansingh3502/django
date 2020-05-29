from django.urls import path
from . import views

app_name = 't1'

urlpatterns = [
	
	path('', views.login, name = 'login'),
	#path('t1/thanks/', views.thanks, name = 'thanks'),


]