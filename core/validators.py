from django.core.exceptions import ValidationError
import re


def iranian_phone_number_validator(value):
    if not re.match(r'^09\d{9}$', value):
        raise ValidationError('Invalid phone number format: your phone number '
                              'must be begin with 09 and have exactly 11 digits')


def country_phone_code_validator(value):
    if not re.match(r'^\+\d{1,3}$', value):
        raise ValidationError('Invalid country phone code: your country phone '
                              'code must be begin with + and have 1,2 or 3 digits')
