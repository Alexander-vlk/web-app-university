from django.db import models
from django.core.validators import RegexValidator


from .validators import validate_fio_format, validate_email, validate_date


class UserProgrammingLanguages(models.Model):
	LANGUAGES_CHOICES = [
        ('PHP', 'PHP'),
        ('Python', 'Python'),
        ('C', 'C'),
        ('C++', 'C++'),
        ('Ruby', 'Ruby'),
        ('JS/TS', 'JS/TS'),
        ('Rust', 'Rust'),
    ]
	programming_languages = models.CharField(max_length=255, verbose_name='Языки программирования')

	class Meta:
		verbose_name = 'Любимые языки программирования'

	def __str__(self):
		return f'{self.programming_languages}'


class UserDataModel(models.Model):
	GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

	fio = models.CharField(max_length=255, validators=[validate_fio_format], verbose_name='ФИО')
	phone = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\d{11}$', message='Введите 10-значный номер телефона')],
						  verbose_name='Номер телефона')
	email = models.EmailField(max_length=100, validators=[validate_email], verbose_name='Электронная почта')
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
	birth = models.DateField(validators=[validate_date], verbose_name='Дата рождения') 
	user_langs = models.ManyToManyField(UserProgrammingLanguages, verbose_name='Любимые языки программирования')
	biography = models.TextField(verbose_name='Биография')

	def __str__(self):
		return f'{self.fio}, {self.phone}, {self.email}'

	class Meta:
		verbose_name = 'Данные пользователя'

