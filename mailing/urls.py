from django.urls import path

from mailing.views.mailing import MailingSettingsCreateView, MailingSettingsListView, MailingSettingsDetailView, \
    MailingSettingsUpdateView, MailingSettingsDeleteView

app_name = 'mailing'

urlpatterns = [
    path('', MailingSettingsListView.as_view(), name='mailingsettings_list'),
    path('create/', MailingSettingsCreateView.as_view(), name='mailingsettings_create'),
    path('detail/<int:pk>/', MailingSettingsDetailView.as_view(), name='mailingsettings_detail'),
    path('update/<int:pk>/', MailingSettingsUpdateView.as_view(), name='mailingsettings_update'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='mailingsettings_delete'),
]
