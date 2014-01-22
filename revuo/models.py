from django.db import models
from django.contrib.auth.models import User
import datetime


class Author(models.Model):
    user = models.OneToOneField(User)
    editor = models.BooleanField(default=False)


    def __unicode__(self):
        return ' '.join([self.user.first_name, self.user.last_name])


class Admin(models.Model):
    user = models.OneToOneField(User)


    def __unicode__(self):
        return ' '.join([self.user.first_name, self.user.last_name])


class Item(models.Model):
    categories = (
        ('N', 'News Item'),
        ('B', 'Blog Post'),
        ('V', 'Video Entry'),
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    authorized = models.BooleanField(default=False)
    author = models.ForeignKey('Author')
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=280)
    text = models.TextField()
    category = models.CharField(max_length=3, choices=categories)


    def __unicode__(self):
        return self.title


def publication_destination(instance, filename):
    return 'documents/' + '_'.join([str(hash(datetime.datetime.now())),filename])


class Publication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    authorized = models.BooleanField(default=False)
    author = models.ForeignKey('Author')
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=280)
    attachment = models.FileField(upload_to=publication_destination)


    def __unicode__(self):
        return self.title
