from django.urls import path
from .import views

app_name = 'user_login'

urlpatterns = [
	
	path('', views.login, name = 'user')
]