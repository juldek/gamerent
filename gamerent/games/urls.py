from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import GameDetailView, GameCreateView, GameListView, GameBorrowView

app_name = "games"
urlpatterns = [
    path('', view=GameListView.as_view(), name='list'),
    path("add/", view=GameCreateView.as_view(), name="add"),
    path("<slug:slug>/borrow", view=GameBorrowView.as_view(), name="borrow"),
    path("<slug:slug>/", view=GameDetailView.as_view(), name="detail"),
]
