from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet, SyncPokemonColorAPIView, PokemonColorViewSet

pokemon_router = DefaultRouter()

pokemon_router.register(r"pokemons", PokemonViewSet, basename="pokemons")
pokemon_router.register(r"colors", PokemonColorViewSet, basename="colors")


urlpatterns = [
    path("", include(pokemon_router.urls)),
    path("sync-color/", SyncPokemonColorAPIView.as_view(), name="sync-color"),
]
