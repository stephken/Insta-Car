from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar, Comment
from insta_post.forms import PostForm, CommentForm


def index(request):
    cars = FavoriteCar.objects.all()
    return render(request, "index.html", {"cars": cars })

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            FavoriteCar.objects.create(poster=data.get('poster'), make=data.get('make'), model=data.get('model'), year=data.get('year'), color=data.get('color'), caption=data.get('caption'), car_image=data.get('car_image'))
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

