from django.core import validators

from os.path import splitext
from rest_framework.exceptions import ValidationError

phone_validator = validators.RegexValidator(r'^\+?\d{9,15}$', 'Invalid phone number', 'invalid')

def validate_file_extension(value, valid_extensions):
    ext = splitext(value.name)[-1]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

def validate_image_extension(value):
    return validate_file_extension(value, ['.jpg', '.png', '.gif', '.jpeg'])