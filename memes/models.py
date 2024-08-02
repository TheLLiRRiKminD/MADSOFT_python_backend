from django.db import models


# Create your models here.

class Meme(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='memes/')
    text = models.TextField()

    def __str__(self):
        return self.title
