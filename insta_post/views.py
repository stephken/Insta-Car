from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar, Comment
from insta_post.forms import PostForm, CommentForm, EditPostForm, EditCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    cars = FavoriteCar.objects.all()
    return render(request, "index.html", {"cars": cars })

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            FavoriteCar.objects.create(poster=request.user, make=data.get('make'), model=data.get('model'), year=data.get('year'), color=data.get('color'), caption=data.get('caption'), car_image=data.get('car_image'))
            return HttpResponseRedirect(reverse("homepage"))
    form = PostForm()
    return render(request, "generic_form.html", {"form": form})

def comment_form_view(request, post_id):
    post = get_object_or_404(FavoriteCar, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = form.save(commit=False)
            comment.post = post
            comment.commenter = request.user
            comment.save()
            return redirect('post', post.id)
    else:
        form = CommentForm()
    return render(request, "generic_form.html", {'form': form})

def photo_detail(request, post_id):
    car = get_object_or_404(FavoriteCar, id=post_id)
    comment_list = Comment.objects.filter(post=car).order_by('-created_on')
    return render(request, 'photo_detail.html', {'car': car, "comment_list": comment_list})

def up_vote(request, post_id):
    vote = FavoriteCar.objects.get(id=post_id)
    vote.total_votes += 1
    vote.save()
    return redirect(request.META.get('HTTP_REFERER'))
    
def down_vote(request, post_id):
    vote = FavoriteCar.objects.get(id=post_id)
    vote.total_votes -= 1
    vote.save()
    return redirect(request.META.get('HTTP_REFERER'))

def del_post(request, post_id):
    post = FavoriteCar.objects.get(id=post_id)
    post.delete()
    return redirect('profile', request.user.username)

def del_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.id == comment.commenter.id:
        comment.delete()
        return redirect('post', comment.post.id)
    else: 
        return HttpResponseForbidden("You do not have permission to delete this comment")

def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk) 
    if request.user.id == comment.commenter.id:
        if request.method == "POST":
            form = EditCommentForm(request.POST, instance=comment)
            if form.is_valid():
                data = form.cleaned_data
                comment.content = data.get('content')
                comment.save()
                return redirect('post', comment.post.id)
        else:
            form = EditCommentForm(instance=comment)
        return render(request, 'generic_form.html', {'form': form})
    else: 
        return HttpResponseForbidden("You do not have permission to edit this comment")
    

def post_edit_view(request, post_id):
    post = FavoriteCar.objects.get(id=post_id)
    if post.poster == request.user:
        if request.method == "POST":
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                data = form.cleaned_data
                post.make = data.get('make')
                post.model = data.get('model')
                post.year = data.get('year')
                post.color = data.get('color')
                if 'car_image' in request.FILES:
                    post.car_image = request.FILES['car_image']
                post.save()
                return redirect('post', post_id)
        else:
            form = EditPostForm(instance=post)
        return render(request, 'generic_form.html', {'form': form})
    else: 
        return HttpResponseForbidden("You do not have permission to edit this post")
    