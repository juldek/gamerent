from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import GameView, GameCreateView, GameListView, GameBorrowView, GameReturnView
from .views_api import game_list, game_detail

app_name = "games"

api_urlpatterns = [
    path("api/", view=game_list),
    path("api/<slug:slug>/", view=game_detail),
]
api_urlpatterns = format_suffix_patterns(api_urlpatterns)

urlpatterns = api_urlpatterns + [
    path('', view=GameListView.as_view(), name='list'),
    path("add/", view=GameCreateView.as_view(), name="add"),
    path("return/", view=GameReturnView.as_view(), name="return"),
    path("<slug:slug>/borrow/", view=GameBorrowView.as_view(), name="borrow"),
    path("<slug:slug>/", view=GameView.as_view(), name="detail"),
]
