from django.views.generic import ListView

from applications.trees.models import Trees


class AllTreesView(ListView):
    template_name = "trees/all.html"
    model = Trees