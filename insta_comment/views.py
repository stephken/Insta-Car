from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar
from insta_comment.models import Comment
from insta_post.forms import PostForm
from insta_comment.forms import CommentForm
# from insta_comment.helpers import add_one


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
    return render(request, "comment_form.html", {'form': form})


def comment_likes(request, pk):
    vote = Comment.objects.get(pk=pk)
    # call function here
    vote.up_votes += 1
    vote.save()
    return redirect(request.META.get('HTTP_REFERER'))


def del_comment(request, pk):
    comment = Comment.objects.filter(pk=pk).first()
    if request.user.id == comment.commenter.id or request.user.id == comment.post.poster.id:
        comment.delete()
        return redirect('post', comment.post.id)
    else: 
        return HttpResponseForbidden("You do not have permission to delete this comment")


def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk) 
    if request.user.id == comment.commenter.id:
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                data = form.cleaned_data
                comment.content = data.get('content')
                comment.save()
                return redirect('post', comment.post.id)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'comment_form.html', {'form': form})
    else: 
        return HttpResponseForbidden("You do not have permission to edit this comment")
