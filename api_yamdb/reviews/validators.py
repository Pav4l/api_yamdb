from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone

from api_yamdb.settings import FIRST_YEAR


def create_slug_validator():
    return RegexValidator(
        regex=r'^[-a-zA-Z0-9_]+$',
        message='Недопустимый символ в графе slug'
    )


def validate_year(value):
    if not FIRST_YEAR <= value <= timezone.now().year:
        raise ValidationError(
            (f'Год произведения должен быть больше {FIRST_YEAR},'
             f'но не больше текущего! У вас: {value}'),
            params={'value': value},
        )


def validate_score(value):
    if not 1 <= value <= 10:
        raise ValidationError(
            ('Рейтинг должен быть от 1 до 10 (границы включены)'),
            params={'value': value},
        )
