from django.urls import path

from .apps import TreesConfig
from .views.all import AllTreesView
from .views.single import SingleTreesView

app_name = TreesConfig.label

urlpatterns = [
    path("", AllTreesView.as_view(), name="all"),
    path("f/<str:pk>/", SingleTreesView.as_view(), name="single"),
]