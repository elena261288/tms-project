from django.urls import path

from applications.contacts.apps import ContactsConfig
from applications.contacts.views import IndexView

app_name = ContactsConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index")]