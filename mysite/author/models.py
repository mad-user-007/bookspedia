from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

#Create your models here
class Author(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    total_books = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
