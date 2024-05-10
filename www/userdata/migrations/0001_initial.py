# Generated by Django 5.0.6 on 2024-05-10 20:30

import django.core.validators
import userdata.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProgrammingLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programming_languages', models.CharField(choices=[('PHP', 'PHP'), ('Python', 'Python'), ('C', 'C'), ('C++', 'C++'), ('Ruby', 'Ruby'), ('JS/TS', 'JS/TS'), ('Rust', 'Rust')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, validators=[userdata.validators.validate_fio_format])),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Введите 10-значный номер телефона', regex='^\\d{10}$')])),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator()])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth', models.DateField(validators=[userdata.validators.validate_date])),
                ('biography', models.TextField()),
                ('user_langs', models.ManyToManyField(to='userdata.userprogramminglanguages')),
            ],
        ),
    ]
