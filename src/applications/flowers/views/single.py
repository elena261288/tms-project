from typing import Dict

from django.views.generic import DetailView

from applications.flowers.models import Flowers


class SingleFlowersView(DetailView):
    model = Flowers
    template_name = "flowers/single.html"





