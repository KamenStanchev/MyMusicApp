from django.core.exceptions import ValidationError


def username_validator(value):
    for letter in value:
        if letter.isdigit() is not True\
                and letter.isalpha() is not True \
                and letter != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def positive_float_validator(value):
    if value < 0:
        raise ValidationError('Price must be positive number!')
