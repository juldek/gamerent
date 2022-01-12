from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View

from .forms import GameBorrowForm
from .models import Game


class GameDetailView(DetailView):
    model = Game


class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['name', 'description', 'max_players', 'img', ]


class GameListView(ListView):
    model = Game


class GameBorrowView(LoginRequiredMixin, View):
    template_name = 'games/game_borrow_form.html'
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
        obj = self.get_object()
        if form.is_valid():
            obj.borrower = request.user
            obj.save()
            return HttpResponseRedirect(reverse('games:detail', kwargs={'slug': obj.slug}))
        return render(request, self.template_name, {'form': form})
