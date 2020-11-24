from django.urls import path

from applications.inform.apps import InformConfig
from applications.inform.views import IndexView

app_name = InformConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index")]