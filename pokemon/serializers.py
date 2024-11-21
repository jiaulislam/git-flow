from rest_framework import serializers

from .models import Pokemon, Color


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"


class PokemonColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"