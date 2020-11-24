from django.views.generic import ListView

from applications.flowers.models import Flowers


class AllFlowersView(ListView):
    template_name = "flowers/all.html"
    model = Flowers