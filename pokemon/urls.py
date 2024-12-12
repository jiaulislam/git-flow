from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet

pokemon_router = DefaultRouter()

pokemon_router.register(r"pokemons", PokemonViewSet, basename="pokemons")


urlpatterns = [
    path("", include(pokemon_router.urls)),
]
