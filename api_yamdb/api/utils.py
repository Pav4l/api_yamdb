from django.core.mail import send_mail


def send_confirmation_code(email, confirmation_code):
    send_mail(
        subject='Код подтверждения',
        message=f'Ваш код подтверждения: {confirmation_code}',
        from_email='from_test@test.ru',
        recipient_list=(email,),
        fail_silently=False,
    )
