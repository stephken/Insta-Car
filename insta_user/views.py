from django.shortcuts import render
from insta_user.models import InstaUser

def index(request):
    data = InstaUser.objects.all()
    return render(request, "index.html", {'data': data})

def profile_view(request, username):
    profile_info = InstaUser.objects.filter(username=username).first()
    return render(request, "user_detail.html", {"info": profile_info})

