from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

from .forms import GameBorrowForm, GameReturnForm
from .models import Game


class GameDetailView(DetailView):
    model = Game


class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['name', 'description', 'max_players', 'img', ]


class GameListView(ListView):
    model = Game


class GameBorrowView(LoginRequiredMixin, View):
    template_name = 'games/game_borrow.html'
    form_class = GameBorrowForm

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = None
        if slug is not None:
            obj = get_object_or_404(Game, slug=slug)
        return obj

    def get(self, request, *args, **kwargs):
        form = self.form_class
        obj = self.get_object()
        return render(request, self.template_name, {'form': form, 'game': obj})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        game = self.get_object()
        if form.is_valid():
            game.borrow(user=request.user)
            return HttpResponseRedirect(reverse('games:detail', kwargs={'slug': game.slug}))
        return render(request, self.template_name, {'form': form})


class GameReturnView(LoginRequiredMixin, ListView):
    template_name = 'games/game_return.html'
    form_class = GameReturnForm
    model = Game

    def get_queryset(self):
        return Game.objects.filter(borrower=self.request.user)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Game.objects.give_back([key for key, value in request.POST.items() if value == 'on'])
            return HttpResponseRedirect(reverse('games:list'))
        return render(request, self.template_name, {'form': form})
