# sample_project/urls.py
from .views import HomeView, CustomCosmographView

from django.urls import path, include

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("", include("django_cosmograph.urls", namespace="django_cosmograph")),
    path(
        "cosmograph/custom-view/",
        CustomCosmographView.as_view(),
        name="cosmograph_custom_view_example",
    ),
]
