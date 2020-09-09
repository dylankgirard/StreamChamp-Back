from django.db import models


class Stream(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    favorites = models.ManyToManyField(Stream, default=[])

    def __str__(self):
        return self.name
