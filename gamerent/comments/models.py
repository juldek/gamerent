from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel


class AbstractComment(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    content = models.TextField()
    resource = models.ForeignKey("Resource", on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.header)
