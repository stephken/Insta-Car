from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar, Comment
from insta_post.forms import PostForm, CommentForm, EditPostForm, EditCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    cars = FavoriteCar.objects.all()
    return render(request, "index.html", {"cars": cars})


def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(request.FILES['car_image'])
        FavoriteCar.objects.create(
            poster=request.user, 
            make=request.POST['make'], 
            model=request.POST['model'], 
            year=request.POST['year'], 
            color=request.POST['color'], 
            caption=request.POST['caption'], 
            car_image=request.FILES['car_image'])
        return HttpResponseRedirect(reverse("homepage"))
    form = PostForm()
    return render(request, "yearmakemodel.html", {"form": form})

def post_edit_view(request, post_id):
    post = FavoriteCar.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        post.make = request.POST['make']
        post.model = request.POST['model']
        post.year = request.POST['year']
        post.color = request.POST['color']
        post.caption = request.POST['caption']
        if 'car_image' in request.FILES:
            post.car_image = request.FILES['car_image']
        post.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = PostForm()
    return render(request, "yearmakemodel.html", {'form': form})

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
    poster_id = car.poster.id
    profile_info = InstaUser.objects.filter(id=poster_id).first()
    comment_list = Comment.objects.filter(post=car).order_by('-created_on')
    return render(request, 'photo_detail.html', {'car': car, "comment_list": comment_list, "info": profile_info})


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
    if request.user.id == post.poster.id:
        post.delete()
        return redirect('profile', request.user.username)
    else: 
        return HttpResponseForbidden("You do not have permission to delete this post")


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
    
    
