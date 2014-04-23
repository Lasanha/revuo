from django.db import models
from django.contrib.auth.models import User
import datetime


class Author(models.Model):
    user = models.OneToOneField(User)
    editor = models.BooleanField(default=False)
    about = models.TextField(max_length=1024)


    def __unicode__(self):
        return ' '.join([self.user.first_name, self.user.last_name])


    def get_url(self):
        return '/staff/{}'.format(self.id)


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


    def authorize(self):
        self.authorized = True


    def __unicode__(self):
        return self.title


    def get_url(self):
        return '/N/{}'.format(self.id)


class BlogItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    authorized = models.BooleanField(default=False)
    author = models.ForeignKey('Author')
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=280)
    text = models.TextField()


    def authorize(self):
        self.authorized = True


    def __unicode__(self):
        return self.title


    def get_url(self):
        return '/B/{}'.format(self.id)


class VideoItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    authorized = models.BooleanField(default=False)
    author = models.ForeignKey('Author')
    title = models.TextField(max_length=140)
    video = models.URLField(max_length=280)
    text = models.TextField()


    def authorize(self):
        self.authorized = True


    def __unicode__(self):
        return self.title


    def get_url(self):
        return '/V/{}'.format(self.id)


def publication_destination(instance, filename):
    return 'revuo/static/documents/' + '_'.join([str(hash(datetime.datetime.now())),filename])


class Publication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    authorized = models.BooleanField(default=False)
    author = models.ForeignKey('Author')
    title = models.TextField(max_length=140)
    description = models.TextField(max_length=280)
    attachment = models.FileField(upload_to=publication_destination)


    def authorize(self):
        self.authorized = True


    def get_url(self):
        return '/P/{}'.format(self.id)


    def get_att_url(self):
        return self.attachment.url[6:]


    def __unicode__(self):
        return self.title
