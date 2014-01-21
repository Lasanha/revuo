from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return ' '.join([self.user.first_name, self.user.last_name])


class Admin(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return ' '.join([self.user.first_name, self.user.last_name])
