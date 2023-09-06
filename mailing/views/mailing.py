from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.forms import MailingSettingsForm
from mailing.models.mailing import MailingSettings


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailingsettings_form.html'
    success_url = reverse_lazy('mailing:mailing_settings_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings
    template_name = 'mailingsettings_list.html'

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.has_perm('mailing.view_mailsettings'):
            return MailingSettings.objects.all()
        queryset = MailingSettings.objects.filter(user=self.request.user, is_active=True)
        return queryset


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings
    template_name = 'mailingsettings_detail.html'


class MailingSettingsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailingsettings_form.html'
    success_url = reverse_lazy('mailing:mailingsettings_list')
    permission_required = 'mailing.change_mailingsettings'

    def has_permission(self):
        obj = self.get_object()
        if self.request.user == obj.user or self.request.user.is_staff:
            return True
        return super().has_permission()


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    template_name = 'mailingsettings_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailingsettings_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404()
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            self.object.delete()
            return self.success_url
        else:
            raise Http404()
