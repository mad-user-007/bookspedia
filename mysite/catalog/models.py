from django.db import models
from django.contrib.auth.models import User
from author.models import Author
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)
    preview = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
