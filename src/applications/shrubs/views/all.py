from django.views.generic import ListView

from applications.shrubs.models import Shrubs


class AllShrubsView(ListView):
    template_name = "shrubs/all.html"
    model = Shrubs