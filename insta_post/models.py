from django.db import models
from datetime import date
from insta_user.models import InstaUser


class FavoriteCar(models.Model):
    make = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=30)
    time_posted = models.DateTimeField(auto_now=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    car_image = models.ImageField(upload_to='images/', null=True, blank=True)
    poster = models.ForeignKey(InstaUser, on_delete=models.CASCADE, related_name="poster")
    caption = models.CharField(max_length=280, null=True, blank=True)

    def __str__(self):
        return self.make, self.model, self.year, self.color, self.time_posted

class Comment(models.Model):
    post = models.ForeignKey(FavoriteCar, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(InstaUser, on_delete=models.CASCADE, related_name="commenter")
    content = models.CharField(max_length = 280)
    created_on = models.DateTimeField(auto_now_add=True)
