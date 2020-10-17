from django.db import models
from datetime import date
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(
        FavoriteCar, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(
        InstaUser, on_delete=models.CASCADE, related_name="commenter")
    content = models.CharField(max_length=280, verbose_name="comment")
    created_on = models.DateTimeField(auto_now_add=True)
    up_votes = models.IntegerField(default=0)
