from django.db import models


class Artist(models.Model):

    name = models.CharField('Исполнитель', max_length=64)

    def __str__(self):
        return self.name


class Album(models.Model):

    name = models.CharField('Альбом', max_length=32)
    year = models.IntegerField('Год выпуска', default=0)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Track(models.Model):

    track = models.CharField('Песня', max_length=64)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.track
