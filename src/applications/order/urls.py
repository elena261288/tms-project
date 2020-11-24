from django.urls import path

from applications.order.apps import OrderConfig
from applications.order.views import IndexView

app_name = OrderConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index")]