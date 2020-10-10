from django.shortcuts import render
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar

def index(request):
    data = InstaUser.objects.all()
    return render(request, "index.html", {'data': data})

# def profile_view(request, username):
#     profile_info = InstaUser.objects.filter(username=username).first()
#     users_uploads = FavoriteCar.objects.filter(poster=request.user.id)
#     return render(request, "user_detail.html", {"info": profile_info, "my_uploads": users_uploads })

def profile_view(request, username):
    context_dict = {}
    user = InstaUser.objects.get(username=username)
    profile_info = InstaUser.objects.filter(username=user).first()
    users_uploads = FavoriteCar.objects.filter(poster=user.id).all()


    context_dict['info'] = profile_info
    context_dict['my_uploads'] = users_uploads

    return render(request, "user_detail.html", context_dict)
