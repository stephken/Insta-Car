from django import forms
from insta_comment.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]

