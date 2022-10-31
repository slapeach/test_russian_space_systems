from django.db import models

from .validators import year_validator


class Artist(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название альбома')
    artist = models.ForeignKey(
        Artist, blank=True, null=True, related_name='artist',
        on_delete=models.CASCADE, verbose_name='Исполнитель произведений'
    )
    year = models.PositiveSmallIntegerField(
        validators=[year_validator],
        verbose_name='Год публикации альбома'
    )

    def __str__(self):
        return f"{self.name}[{self.year}]"


class Track(models.Model):
    name = models.CharField(max_length=150)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
