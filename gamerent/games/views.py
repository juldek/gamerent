from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from .models import Game


class GameDetailView(DetailView):
    model = Game

