from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def validate_custom_email(value):
    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError("Неверный адрес электронной почты")


def validate_fio_format(value):
    parts = value.split(" ")
    if len(parts) < 3:
        raise ValidationError("ФИО должно состоять из трех слов: имя, фамилия и отчество")


def validate_date(value):
    if value.year <= 1900:
        raise ValidationError("Введен неверный год рождения")