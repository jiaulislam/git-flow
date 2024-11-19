from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=80)
    base_experience = models.IntegerField(default=0)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    is_default = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)
