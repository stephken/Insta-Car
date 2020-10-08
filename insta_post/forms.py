from django import forms
from insta_post.models import FavoriteCar

class PostForm(forms.ModelForm):
    class Meta:
        model = FavoriteCar
        fields = ["make", "model", "year", "color", "car_image"]
