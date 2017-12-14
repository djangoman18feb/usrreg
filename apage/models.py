from django.db import models
from django.core.urlresolvers import reverse   #to divert them to any page(detail page)after they submit the model form

# Create your models here.
class Quote(models.Model):
    text = models.CharField(max_length=1000, default="Write right on me...Pour your heart")
    tags = models.CharField(max_length=1000, default="Morality")

    def get_absolute_url(self):
        return reverse('apage:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.text[0:30] + self.tags

class About_art(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=100, default="Anonumous")
    artist_title = models.CharField(max_length=100, default="The Seeker")
    artist_image = models.CharField(max_length=150)
    artist_des = models.CharField(max_length=1000)
    artist_story = models.CharField(max_length=3000)

    def __str__(self):
        return self.artist_des[0:50]

#
# class User_Profile(models.Model):
#     user_name = models.CharField(max_length=100, default="Anonumous")
#     user_title = models.CharField(max_length=100, default="The Seeker")
#     user_image = models.CharField(max_length=150)
#     user_lct = models.CharField(max_length=600)
#     user_gen = models.CharField(max_length=600)
#     user_age = models.CharField(max_length=600)
#     user_int = models.CharField(max_length=600)
#     user_goal = models.CharField(max_length=600)
#     user_des = models.CharField(max_length=1000)
#     user_quote = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.user_name + self.user_title
#
#     def get_absolute_url(self):
#         return reverse('apage:profile', kwargs={'pk': self.pk})
