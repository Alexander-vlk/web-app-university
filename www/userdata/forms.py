from django.forms import ModelForm


from .models import UserDataModel


class UserDataForm(ModelForm):
	class Meta:
		model = UserDataModel
		fields = ['fio', 'phone', 'email', 'gender', 'birth', 'user_langs', 'biography']