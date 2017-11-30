from django.db import models

# Create your models here.
class Quote(models.Model):
    text = models.CharField(max_length=3000)
    tag = models.CharField(max_length=100, default="Unknown")
    artist = models.CharField(max_length=100, default="Anonumous")


    def __str__(self):
        return self.artist[0:10] + self.tag

class About_art(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    artist_image = models.CharField(max_length=150)
    artist_his = models.CharField(max_length=3000)


    def __str__(self):
        return self.artist_his[0:10]
