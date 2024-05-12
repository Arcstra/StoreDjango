from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings
from celery import shared_task


@shared_task
def sendCodeToEmail(email, code):
    send_mail(
        "Подтверждение электронной почты",
        f"Ваш код: {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=True,
    )