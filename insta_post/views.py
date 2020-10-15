from django.shortcuts import render
from insta_post.models import FavoriteCar



##test

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
