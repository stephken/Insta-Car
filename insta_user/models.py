from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class InstaUser(AbstractUser):
    bio = models.TextField(null=True, blank=True, verbose_name="About Me")
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    joined_date = models.DateField(auto_now_add=True)


class FavoriteCar(models.Model):
    make = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=30)
    time_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.make, self.model, self.year, self.color, self.time_posted


class UserEmail(models.Model):
    email = models.EmailField(max_length=200)
    author = models.ForeignKey(InstaUser, on_delete=models.CASCADE, related_name="author", default="")

    def __str__(self):
        return self.email
