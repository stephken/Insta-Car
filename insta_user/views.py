from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar
from insta_user.forms import EditProfileForm


def index(request):
    data = InstaUser.objects.all()
    return render(request, "index.html", {'data': data})


# @login_required
def profile_view(request, username):
    context_dict = {}
    users_info = InstaUser.objects.filter(username=username).first()
    profile_info = InstaUser.objects.filter(username=users_info).first()
    users_uploads = FavoriteCar.objects.filter(poster=users_info).all()
    count = FavoriteCar.objects.filter(poster=users_info).count
    user_following = request.user.following.all()
    context_dict['info'] = profile_info
    context_dict['my_uploads'] = users_uploads
    context_dict['count'] = count
    context_dict['user_following'] = user_following
    return render(request, "user_detail.html", context_dict)


# @login_required
def profile_edit_view(request, username):
    edit = get_object_or_404(InstaUser, username=username)
    if edit.username == request.user.username:
        if request.method == "POST":
            form = EditProfileForm(request.POST, request.FILES, instance=edit)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.save()
                return redirect('profile', username)
        else:
            form = EditProfileForm(instance=edit)
        return render(request, 'profile_form.html', {'form': form})
    else: return HttpResponseForbidden("You do not have permission to edit this post")
                
    form = EditProfileForm()
    return render(request, 'profile_form.html', {'form': form} )


# @login_required
def del_user(request, username):    
    u = InstaUser.objects.get(username=username)
    if u.is_staff:
        return HttpResponseForbidden("Staff profiles cannot be deleted from the browser. See an admin")
    elif u.username == request.user.username:
        u.delete()
        messages.success(request, "The user is deleted")
        return redirect('homepage')   
    else: 
        return HttpResponseForbidden("You do not have permission to delete this user")


# @login_required
class FollowView(TemplateView):
    def get(self, request, follow_id):
        signed_in_user = InstaUser.objects.filter(username=request.user.username).first()
        follow = InstaUser.objects.filter(id=follow_id).first()
        if follow_id != request.user.id:
            signed_in_user.following.add(follow)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# @login_required
class UnfollowView(TemplateView):
    def get(self, request, unfollow_id):
        signed_in_user = request.user
        unfollow = InstaUser.objects.filter(id=unfollow_id).first()
        signed_in_user.following.remove(unfollow)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
