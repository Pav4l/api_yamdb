from django.core.validators import RegexValidator


def username_validator():
    return RegexValidator(
        regex=r'^[\w.@+-]+$',
        message='Недопустимое имя пользователя'
    )
