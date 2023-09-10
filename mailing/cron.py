from mailing.models.mailing import MailingSettings
from mailing.services import send_mailing


def daily_send():
    for mailing in MailingSettings.objects.filter(frequency='daily'):
        mailing.status = 'started'
        mailing.save()
        log = send_mailing(mailing)
        mailing.status = 'completed'
        mailing.save()


def weekly_send():
    for mailing in MailingSettings.objects.filter(frequency='weekly'):
        mailing.status = 'started'
        mailing.save()
        log = send_mailing(mailing)
        mailing.status = 'completed'
        mailing.save()


def monthly_send():
    for mailing in MailingSettings.objects.filter(frequency='monthly'):
        mailing.status = 'started'
        mailing.save()
        log = send_mailing(mailing)
        mailing.status = 'completed'
        mailing.save()
