from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from insta_user.models import InstaUser
from insta_post.models import FavoriteCar
from insta_post.forms import PostForm


def index(request):
    cars = FavoriteCar.objects.all()
    return render(request, "index.html", {"cars": cars })

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            FavoriteCar.objects.create(make=data.get('make'), model=data.get('model'), year=data.get('year'), color=data.get('color'), car_image=data.get('car_image'))
            return HttpResponseRedirect(reverse("homepage"))
    form = PostForm()
    return render(request, "generic_form.html", {"form": form})
    
def photo_detail(request, post_id):
    car = get_object_or_404(FavoriteCar, id=post_id)
    return render(request, 'photo_detail.html', {'car': car})

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

