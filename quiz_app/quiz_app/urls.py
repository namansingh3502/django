from django.contrib import admin
from django.urls import path,include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('login.urls')),
	path('creator/', include('creator.urls')),
	#path('participant', include('participant.urls')),   
]