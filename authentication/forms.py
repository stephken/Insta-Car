from django import forms
from insta_user.models import InstaUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = InstaUser
        fields = ['username', 'password', 'bio', 'website', 'profile_image']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
