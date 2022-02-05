from django.urls import path

from .views import GameDetailView, GameCreateView, GameListView, GameBorrowView, GameReturnView
from .views_api import game_list, game_detail

app_name = "games"
urlpatterns = [
    path("api/", view=game_list),
    path("api/<slug:slug>/", view=game_detail),
    path('', view=GameListView.as_view(), name='list'),
    path("add/", view=GameCreateView.as_view(), name="add"),
    path("return/", view=GameReturnView.as_view(), name="return"),
    path("<slug:slug>/borrow/", view=GameBorrowView.as_view(), name="borrow"),
    path("<slug:slug>/", view=GameDetailView.as_view(), name="detail"),
]
