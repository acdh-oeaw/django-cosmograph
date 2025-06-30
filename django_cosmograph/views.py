from django.views.generic import TemplateView
import json


class CosmographView(TemplateView):
    template_name = "django_cosmograph/cosmograph.html"

    def get_nodes_links(self):
        # Expect JSON strings in GET params
        nodes_json = self.request.GET.get("nodes", "[]")
        links_json = self.request.GET.get("links", "[]")
        try:
            nodes = json.loads(nodes_json)
            links = json.loads(links_json)
        except json.JSONDecodeError:
            nodes, links = [], []

        print("NODES", nodes, "LINKS", links)
        return nodes, links

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nodes, links = self.get_nodes_links()
        context["nodes_json"] = json.dumps(nodes)
        context["links_json"] = json.dumps(links)
        return context
