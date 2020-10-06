from django.shortcuts import render
from insta_user.models import InstaUser

def index(request):
    data = InstaUser.objects.all()
    return render(request, "index.html", {'data': data})

