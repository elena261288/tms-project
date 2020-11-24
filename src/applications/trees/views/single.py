from django.views.generic import DetailView

from applications.trees.models import Trees


class SingleTreesView(DetailView):
    model = Trees
    template_name = "trees/single.html"




