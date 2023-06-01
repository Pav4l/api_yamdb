from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone


def create_slug_validator():
    return RegexValidator(
        regex=r'^[-a-zA-Z0-9_]+$',
        message='Недопустимый символ в графе slug'
    )


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            ('Год %(value)s больше текущего!'),
            params={'value': value},
        )


def validate_score(value):
    if value > 10 or value < 1:
        raise ValidationError(
            ('Рейтинг должен быть от 1 до 10 (границы включены)'),
            params={'value': value},
        )
