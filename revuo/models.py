from django.db import models
from django.contrib.auth.models import User
import datetime


class Author(models.Model):
    user = models.OneToOneField(User)
    editor = models.BooleanField(default=False)
    about = models.TextField(max_length=1024)


    def __unicode__(self):
        return ' '.join([self.user.first_name, self.user.last_name])


class Admin(models.Model):
    user = models.OneToOneField(User)


    def __unicode__(self):
        return ' '.join([self.user.first_name, self.user.last_name])


class NewsItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    authorized = models.BooleanField(default=False)
    author = models.ForeignKey('Author')
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=280)
    text = models.TextField()


    def __unicode__(self):
        return self.title


class BlogItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    authorized = models.BooleanField(default=False)
    author = models.ForeignKey('Author')
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=280)
    text = models.TextField()


    def __unicode__(self):
        return self.title


class VideoItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    authorized = models.BooleanField(default=False)
    author = models.ForeignKey('Author')
    title = models.TextField(max_length=140)
    video = models.URLField(max_length=280)
    text = models.TextField()


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
