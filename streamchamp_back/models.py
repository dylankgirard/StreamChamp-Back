from django.db import models
from django.contrib.postgres.fields import ArrayField


class Stream(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.CharField(max_length=100)
    favorites = ArrayField(models.TextField(), default=list)

    def __str__(self):
        return self.name
