from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


class MailingCreateView(LoginRequiredMixin, CreateView):
    pass

