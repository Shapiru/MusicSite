from django.contrib.auth.models import User
from django.db import models

# Create your models here.
GENRE=(
    ('Unknown', 'unknown'),
    ('Rap','rap'),
    ('Riddim','riddim'),
    ('RnB','rnb'),
    ('Local','local'),
    ('Pop','pop'),
    ('House','house'),
)

class Album(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    artist=models.CharField(max_length=40)
    year=models.CharField(max_length=4)
    cover=models.ImageField()
    genre=models.CharField(choices=GENRE, max_length=30,default='unknown')

    def __str__(self):
        return self.name

class Song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    audio=models.FileField()

    def __str__(self):
        return self.name

