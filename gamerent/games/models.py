from django.conf import settings
from django.db import models

# Create your models here.
from autoslug import AutoSlugField
from django.urls import reverse
from model_utils.models import TimeStampedModel


class Game(TimeStampedModel):
    name = models.CharField("Game name", max_length=255)
    slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from='name')
    max_players = models.IntegerField("Max number of players")
    description = models.TextField("Description", blank=True)
    img = models.ImageField(upload_to='games/', blank=True)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('games:detail', kwargs={"slug": self.slug})

    def __str__(self):
        return str(self.name)



