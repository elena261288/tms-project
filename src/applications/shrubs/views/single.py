from typing import Dict

from django.urls import reverse_lazy
from django.views.generic import  DetailView

from applications.shrubs.models import Shrubs


class SingleShrubsView(DetailView):
    model = Shrubs
    template_name = "shrubs/single.html"



