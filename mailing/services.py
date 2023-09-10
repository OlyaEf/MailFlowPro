from django.core.mail import send_mail
from django.conf import settings
from .models.mailing_log import MailingLog


def send_mailing(mailing_object):
    emails = [client.email for client in mailing_object.client.all()]
    try:
        send_mail(
            subject=mailing_object.message.subject,
            message=mailing_object.message.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails,
        )
        status_attempt = 'success'
        answer_server = 'Email sent successfully'
    except Exception as e:
        status_attempt = 'error'
        answer_server = str(e)

    log = MailingLog.objects.create(
        status_attempt=status_attempt,
        answer_server=answer_server,
        mailing=mailing_object,
    )

    return log