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
    programming_languages = models.CharField(max_length=255, choices=LANGUAGES_CHOICES)


class UserDataModel(models.Model):
	GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

	fio = models.CharField(max_length=255, validators=[validate_fio_format])
	phone = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\d{10}$', message='Введите 10-значный номер телефона')])
	email = models.EmailField(max_length=100, validators=[validate_email])
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	birth = models.DateField(validators=[validate_date]) 
	user_langs = models.ManyToManyField(UserProgrammingLanguages)
	biography = models.TextField()

	def __str__(self):
		return f'{self.fio}, {self.phone}, {self.email}'


