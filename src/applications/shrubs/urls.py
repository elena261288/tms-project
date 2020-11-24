from django.urls import path

from .apps import ShrubsConfig
from .views.all import AllShrubsView
from .views.single import SingleShrubsView

app_name = ShrubsConfig.label

urlpatterns = [
    path("", AllShrubsView.as_view(), name="all"),
    path("s/<str:pk>/", SingleShrubsView.as_view(), name="single"),
]