from django.conf import settings
from django.db import models

from constants import NULLABLE


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.full_name} {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class MailingSettings(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    STATUS_CHOICES = [
        ('created', 'Created'),
        ('started', 'Started'),
        ('completed', 'Completed'),
    ]

    sending_time = models.TimeField(verbose_name='время рассылки')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='статус')

    client = models.ManyToManyField(Client, max_length=150, verbose_name='клиент')  # Связь многие ко многим с моделью Client
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, max_length=150, verbose_name='пользователь')  # Связь многие к одному с моделью User

    def __str__(self):
        return (f"Сообщение отправлено для {self.client.email}, "
                f"периодичность рассылки {self.frequency}, статус {self.status}")

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name='тема', default='No subject')
    body = models.TextField(verbose_name='текст письма')

    def __str__(self):
        return f' Тема: {self.subject}. Содержание: {self.body}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingLog(models.Model):
    STATUS_CHOICES = [
        ('success', 'Success'),
        ('error', 'Error'),
        ('pending', 'Pending'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    response = models.TextField()
    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'

    def __str__(self):
        return f"Log for {self.mailing.client.full_name} at {self.timestamp}"
