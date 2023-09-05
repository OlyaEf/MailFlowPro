from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from mailing.models import Client, MailingSettings, Message


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = Client.objects.all()
        context['sent_mailing'] = MailingSettings.objects.all()
        context['message'] = Message.objects.all()

        return context


class GuestPageView(TemplateView):
    template_name = 'core/home_guest.html'


def contacts_view(request):
    return render(request, 'core/contacts.html')
