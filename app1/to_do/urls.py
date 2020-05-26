from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
	
	#path('', views.home, name = 'home'),
	path('', views.login, name = 'login'),

	path('completed/', views.completed, name = 'completed'),

	path('newtask/', views.newtask, name='newtask'),

	path('<int:task_id>/change/', views.change, name='change')
]