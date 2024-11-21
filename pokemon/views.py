import requests
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Color, Pokemon
from .serializers import PokemonColorSerializer, PokemonSerializer


class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = PokemonColorSerializer

    @action(detail=False, methods=["get"], url_path="sync")
    def sync_pokemon_colors(self, request):
        try:
            res = requests.get("https://pokeapi.co/api/v2/pokemon-color/black")
            res.raise_for_status()
            for pokemon in res.json()["names"]:
                name = pokemon["name"]
                language = pokemon["language"]["name"]
                color = res.json()["name"]
                Color.objects.create(name=name, language=language, color=color)
            return Response(
                {"message": "Pokemon colors synced successfully!"},
                status=status.HTTP_200_OK,
            )
        except requests.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
