from django.urls import path

from .views import GameDetailView

app_name = "games"
urlpatterns = [
    path("<slug:slug>/", view=GameDetailView.as_view(), name="detail"),
]
