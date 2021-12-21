from django.db import models

# Create your models here.
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Game(TimeStampedModel):
    name = models.CharField("Game name", max_length=255)
    slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from='name')
    max_players = models.IntegerField("Max number of players")
    description = models.TextField("Description", blank=True)



