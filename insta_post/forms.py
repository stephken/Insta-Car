from django import forms
from insta_post.models import FavoriteCar

class PostForm(forms.ModelForm):
    year= forms.ChoiceField(label='year', widget=forms.Select(attrs={"name": "car-years", "id": "car-years"}))
    make= forms.CharField(label='make', widget=forms.Select(attrs={"name": "car-makes", "id": "car-makes"}))
    model= forms.ChoiceField(label='model', widget=forms.Select(attrs={"name": "car-models", "id": "car-models"}))

    class Meta:
        model = FavoriteCar
        fields = ["year", "make", "model", "color", "caption", "car_image"]

