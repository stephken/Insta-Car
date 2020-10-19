from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar
from insta_comment.models import Comment
from insta_post.forms import PostForm
from insta_comment.forms import CommentForm
# from insta_comment.helpers import add_one


class IndexView(TemplateView):
  
    def get(self,request):
        cars = FavoriteCar.objects.all()
        return render(request, "index.html", {"cars": cars})


# @login_required
def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if 'car_image' not in request.FILES:
            return HttpResponse("Please select a photo")
        new_post = FavoriteCar.objects.create(
            poster=request.user, 
            make=request.POST['make'], 
            model=request.POST['model'], 
            year=request.POST['year'], 
            color=request.POST['color'], 
            caption=request.POST['caption'], 
            car_image=request.FILES['car_image']) 
        return redirect('post', new_post.pk)
    form = PostForm()
    return render(request, "yearmakemodel.html", {"form": form})


# @login_required
def post_edit_view(request, post_id):
    post = FavoriteCar.objects.get(id=post_id)
    if post.poster == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            post.make = request.POST['make']
            post.model = request.POST['model']
            post.year = request.POST['year']
            post.caption = request.POST['caption']
            post.color = request.POST['color']
            if 'car_image' in request.FILES:
                post.car_image = request.FILES['car_image']
            post.save()
            form = PostForm()
            return redirect('post', post_id)
        else:
            form = PostForm(instance=post)
        return render(request, "yearmakemodel.html", {'form': form})
    else: 
        return HttpResponseForbidden("You do not have permission to edit this post")


# @login_required
def photo_detail(request, post_id):
    car = get_object_or_404(FavoriteCar, id=post_id)
    poster_id = car.poster.id
    profile_info = InstaUser.objects.filter(id=poster_id).first()
    comment_list = Comment.objects.filter(post=car).order_by('-created_on')
    return render(request, 'photo_detail.html', {'car': car, "comment_list": comment_list, "info": profile_info})


# @login_required
def up_vote(request, post_id):
    vote = FavoriteCar.objects.get(id=post_id)
    # call helper function here
    vote.up_votes += 1
    vote.save()
    return redirect(request.META.get('HTTP_REFERER'))


# @login_required
def del_post(request, post_id):
    post = FavoriteCar.objects.get(id=post_id)
    if request.user.id == post.poster.id:
        post.delete()
        return redirect('profile', request.user.username)
    else: 
        return HttpResponseForbidden("You do not have permission to delete this post")
     

def handler404(request, exception):
    return render(request, '404.html', status=404)
    
def handler500(request):
    return render(request, '500.html', status=500)
