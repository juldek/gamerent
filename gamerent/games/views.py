from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, CreateView, ListView
from .models import Game


class GameDetailView(DetailView):
    model = Game


class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'description', 'max_players', 'img', ]


class GameListView(ListView):
    model = Game
