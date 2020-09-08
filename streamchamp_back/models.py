from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    favorites = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stream(models.Model):
    name = models.CharField(max_length=100)
    favorited = models.ManyToManyField(User)

    def __str__(self):
        return f'Hello World {self.name} {self.favorited}'