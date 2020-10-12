from django.shortcuts import render
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar
from insta_user.forms import EditProfileForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages


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


def profile_edit_view(request, username):
    user = InstaUser.objects.filter(username=username).first()
    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
                data = form.cleaned_data
                user.bio = data.get('bio')
                user.website = data.get('website')
                if 'profile_image' in request.FILES:
                    user.profile_image = request.FILES['profile_image']
                user.save()
                return HttpResponseRedirect(reverse('homepage'))

    form = EditProfileForm()
    return render(request, 'generic_form.html', {'form': form} )

def del_user(request, username):    
    u = InstaUser.objects.get(username = username)
    u.delete()
    messages.success(request, "The user is deleted")
    return render(request, 'index.html')
