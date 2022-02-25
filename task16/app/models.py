from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver
from django.template.loader import render_to_string
from django_rest_passwordreset.signals import reset_password_token_created


class CustomUser(AbstractUser):
    reign_name = models.CharField(max_length=200)

    def __str__(self):
        return self.email


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_token': reset_password_token.key
    }
    email_html_message = render_to_string('email/password reset.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Nosheen"),
        # message:
        email_plaintext_message,
        # from:
        "Blaque Fitness",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()