from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Count


from .models import UserDataModel, UserProgrammingLanguages
from .forms import UserDataForm, AuthUserForm, UserRegisterForm

def home_page(request):
	return render(request, 'home.html', {})

class UserAdminView(ListView):
	model = UserDataModel
	template_name = 'admin.html'

	def get_queryset(self):
		return UserDataModel.objects.all()
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_data'] = UserDataModel.objects.all()
		context['users'] = User.objects.all()
		context['language_stats'] = UserProgrammingLanguages.objects.annotate(num_users=Count('userdatamodel')).order_by('-num_users')
		return context

class UserDataView(FormView):
	template_name = 'index.html'
	form_class = UserDataForm
	success_url = '/web_4'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(self.request.user, 'XXXXX')
		if self.request.user.id != None:
			user_items = UserDataModel.objects.filter(creator=self.request.user)
		else:
			user_items = ''
		context['user_items'] = user_items
		return context
	
	def get_initial(self):
		initial = super().get_initial()
        # Попытка получения данных из cookies
		initial['fio'] = self.request.COOKIES.get('fio', '')
		initial['phone'] = self.request.COOKIES.get('phone', '')
		initial['email'] = self.request.COOKIES.get('email', '')

		return initial

	def form_valid(self, form):
		
		response = super().form_valid(form)
		response.set_cookie('phone', form.cleaned_data['phone'], max_age=80)
		response.set_cookie('email', form.cleaned_data['email'], max_age=80)
		if self.request.user.id != None:
			form.instance.creator = self.request.user
		form.save()

		return response
	

class UserLoginView(LoginView):
	template_name = 'login.html'
	success_url = '../web_4'
	def get_success_url(self) -> str:
		return self.success_url

class UserRegisterView(CreateView):
	model = User
	template_name = 'register.html'
	success_url = 'login'
	form_class = UserRegisterForm
	success_msg = 'Success!'

class UserLogoutView(LogoutView):
	next_page = reverse_lazy('login')
	redirect_field_name = 'login'
	def get_redirect_url(self):
		return self.next_page
	def get_success_url(self):
		return self.get_redirect_url() or self.get_default_redirect_url()
	

def logout_view(request):
    logout(request)
    # Перенаправление на главную страницу или другую страницу после выхода
    return redirect('web_4/')


class UpdateUserDataView(UpdateView):
	model = UserDataModel
	form_class = UserDataForm
	template_name = 'edit.html'
	success_url = '/web_4'

class DeleteUserDataView(DeleteView):
	model = UserDataModel
	success_url = '/web_4'
	template_name = 'delete.html'