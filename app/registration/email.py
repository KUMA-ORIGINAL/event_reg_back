from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import TeamCaptain

def send_captain_emails(captains):
    for captain in captains:
        subject = 'Уведомление для капитана команды'
        html_message = render_to_string('email/team_captain_email.html', {'captain': captain})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [captain.email]

        send_mail(
            subject,
            plain_message,  # plain text version
            from_email,
            recipient_list,
            html_message=html_message  # HTML version
        )