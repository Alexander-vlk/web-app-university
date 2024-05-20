from django.urls import path


from .views import UserDataView, home_page, UserLoginView, UserRegisterView,UserLogoutView, logout_view


urlpatterns = [
	path('web_4/', UserDataView.as_view(), name='home'),
	path('web_5/', home_page, name='web_5'),
	path('web_5/login', UserLoginView.as_view(), name='login'),
	path('web_5/register', UserRegisterView.as_view(), name='register'),
	path('logout', logout_view, name='logout'),
]