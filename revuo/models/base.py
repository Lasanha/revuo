from django.db import models


class BaseDatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
