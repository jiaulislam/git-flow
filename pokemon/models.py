from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=80)
    base_experience = models.IntegerField(default=0)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    is_default = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)
    species = models.CharField(max_length=80, null=True, blank=True)
    sprites = models.JSONField(null=True, blank=True)
    waka_waka = models.CharField(max_length=255, default="WAKA_WAKA")


class PokemonType(models.Model):
    name = models.CharField(max_length=80)
    pokemon = models.ManyToManyField(Pokemon, related_name="types")
