from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    max_players = serializers.IntegerField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    #img = serializers.ImageField(upload_to='games/', allow_blank=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.max_players = validated_data.get('max_players', instance.max_players)
        instance.description = validated_data.get('description', instance.description)
        #instance.img = validated_data.get('img', instance.img)
        instance.save()
        return instance
