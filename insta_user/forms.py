from django import forms
from insta_user.models import InstaUser, UserEmail



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = InstaUser
        fields = ('website', 'bio', 'profile_image')