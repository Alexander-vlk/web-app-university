
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import UserDataForm

def home_page(request):

	return render(request, 'index.html', {})


class UserDataView(FormView):
	template_name = 'index.html'
	form_class = UserDataForm
	success_url = '/'
	
	
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
		form.save()

		return response
