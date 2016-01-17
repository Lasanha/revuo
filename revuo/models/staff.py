from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField(max_length=1024)

    def __str__(self):
        return self.user.get_full_name()

    def get_url(self):
        return reverse('revuo:staff_view', kwargs={'staff_id': str(self.id)})
