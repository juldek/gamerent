from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import GameDetailView, GameCreateView

app_name = "games"
urlpatterns = [
    path("add/", view=GameCreateView.as_view(), name="add"),
    path("<slug:slug>/", view=GameDetailView.as_view(), name="detail"),
]
