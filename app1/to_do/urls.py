from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
	
	path('', views.home, name = 'home'),

	path('completed/', views.completed, name = 'completed'),

	path('newtask/', views.newtask, name='newtask'),
]