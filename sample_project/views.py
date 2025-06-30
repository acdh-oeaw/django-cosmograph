from django.views.generic import TemplateView
from django_cosmograph.views import CosmographView
import random


class HomeView(TemplateView):
    template_name = "base.html"


class CustomCosmographView(CosmographView):

    def get_nodes_links(self):
        def generate_graph(num_nodes=1000, num_links=3000):
            colours = ["cyan", "crimson", "goldenrod"]
            nodes = [
                {
                    "id": i,
                    "label": f"Node {i}",
                    "colour": colours[random.randint(0, len(colours) - 1)],
                }
                for i in range(num_nodes)
            ]
            links = []

            for _ in range(num_links):
                source = random.randint(0, num_nodes - 1)
                target = random.randint(0, num_nodes - 1)
                if source != target:
                    links.append({"source": source, "target": target})

            return nodes, links

        return generate_graph(3000, 4000)
