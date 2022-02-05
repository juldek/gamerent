from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser

from .serializers import GameSerializer
from .models import Game


@api_view(['GET', 'POST'])
def game_list(request, format=None):
    if request.method == "GET":
        games = Game.objects.all()
        serialized = GameSerializer(games, many=True)
        return Response(serialized.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serialized = GameSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, slug, format=None):
    game = get_object_or_404(Game, slug=slug)
    if request.method == "GET":
        return Response(GameSerializer(game).data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serialized = GameSerializer(game, data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





