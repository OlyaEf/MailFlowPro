from django.contrib import admin
from .models import Client, MailingLog, Message, MailingSettings

admin.site.register(Client)
admin.site.register(MailingLog)
admin.site.register(Message)
admin.site.register(MailingSettings)
