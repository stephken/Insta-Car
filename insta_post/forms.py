from django import forms
from insta_post.models import FavoriteCar, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = FavoriteCar
        fields = ["make", "model", "year", "color", "caption", "car_image"]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]

class EditPostForm(forms.ModelForm):
    make = forms.CharField(max_length=80, required=False)
    model = forms.CharField(max_length=80, required=False)
    year = forms.CharField(max_length=4, required=False)
    color = forms.CharField(max_length=30, required=False)
    caption = forms.CharField(max_length=280, required=False)

    class Meta:
        model = FavoriteCar
        fields = ('make', 'model', 'year', 'color', 'caption', 'car_image')

class EditCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]
