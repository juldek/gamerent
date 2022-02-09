from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin

from .forms import GameBorrowForm, GameReturnForm, GameCommentForm
from .models import Game, GameComment


class GameDetailView(DetailView):
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GameCommentForm()
        return context


class GameCommentFormView(SingleObjectMixin, FormView):
    template_name = 'games/game_detail.html'
    form_class = GameCommentForm
    model = Game

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        print(request.POST)
        self.object = self.get_object()
        self.object.add_comment(request.user, request.POST['header'], request.POST['content'])

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('games:detail', kwargs={'slug': self.object.slug})


class GameView(View):
    def get(self, request, *args, **kwargs):
        view = GameDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = GameCommentFormView.as_view()
        return view(request, *args, **kwargs)


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
