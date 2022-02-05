from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser

from .serializers import GameSerializer
from .models import Game


@csrf_exempt
def game_list(request):
    print("here {}".format(request))
    print(request.method)
    print(request.POST)
    if request.method == "GET":
        games = Game.objects.all()
        serialized = GameSerializer(games, many=True)
        return JsonResponse(serialized.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serialized = GameSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data, status=201)
        return JsonResponse(serialized.errors, status=400)


@csrf_exempt
def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == "GET":
        return JsonResponse(GameSerializer(game).data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serialized = GameSerializer(game, data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data)
        return JsonResponse(serialized.errors, status=400)

    if request.method == "DELETE":
        game.delete()
        return HttpResponse(status=204)





