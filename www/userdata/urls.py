from django.urls import path


from . import views


urlpatterns = [
	path('web_4/', views.UserDataView.as_view(), name='home'),
	path('web_4/<int:pk>', views.UpdateUserDataView.as_view(), name='data'),
	path('web_4/<int:pk>/delete', views.DeleteUserDataView.as_view(), name='delete'),
	path('web_5/', views.home_page, name='web_5'),
	path('web_5/login', views.UserLoginView.as_view(), name='login'),
	path('web_5/register', views.UserRegisterView.as_view(), name='register'),
	path('logout', views.logout_view, name='logout'),
	path('admin/', views.UserAdminView.as_view(), name='admin')
]