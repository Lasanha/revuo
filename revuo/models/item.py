from django.core.urlresolvers import reverse
from django.db import models

from .base import BaseDatedModel
from .staff import Staff


class BaseItem(BaseDatedModel):
    authorized = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    author = models.ForeignKey(Staff)
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=280)

    class Meta:
        abstract = True

    def authorize(self):
        self.authorized = True

    def suspend(self):
        self.authorized = False

    def __str__(self):
        return self.title

    def get_url(self):
        raise NotImplementedError


class NewsItem(BaseItem):
    category = 'N'
    text = models.TextField()

    def get_url(self):
        return reverse('revuo:item_view', kwargs={'category': self.category, 'item_id': str(self.id)})


class BlogItem(BaseItem):
    category = 'B'
    text = models.TextField()

    def get_url(self):
        return reverse('revuo:item_view', kwargs={'category': self.category, 'item_id': str(self.id)})


def publication_destination(instance, filename):
    return '_'.join([str(instance.author.id),filename])


class Publication(BaseItem):
    category = 'P'
    attachment = models.FileField(upload_to=publication_destination)

    def get_url(self):
        return reverse('revuo:item_view', kwargs={'category': self.category, 'item_id': str(self.id)})
