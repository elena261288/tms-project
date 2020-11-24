from django.urls import path

from .apps import FlowersConfig
from .views.all import AllFlowersView
from .views.single import SingleFlowersView

app_name = FlowersConfig.label

urlpatterns = [
    path("", AllFlowersView.as_view(), name="all"),
    path("f/<str:pk>/", SingleFlowersView.as_view(), name="single"),
]