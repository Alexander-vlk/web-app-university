from django.contrib import admin
from django.urls import path, include


from userdata import urls

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('userdata.urls'), name='userdata')
]
