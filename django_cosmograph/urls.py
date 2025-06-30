from django.urls import path
from .views import CosmographView

app_name = "django_cosmograph"

urlpatterns = [
    path("cosmograph/", CosmographView.as_view(), name="cosmograph"),
]
