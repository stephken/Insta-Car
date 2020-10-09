from django import forms
from insta_post.models import FavoriteCar, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = FavoriteCar
        fields = ["poster", "make", "model", "year", "color", "caption", "car_image"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["commenter", "content"]
