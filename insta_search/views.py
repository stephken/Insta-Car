from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.db.models import Q 
from insta_post.models import FavoriteCar



class SearchResultsView(ListView):
    model = FavoriteCar
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = FavoriteCar.objects.filter(
            Q(model__icontains=query)
        )
        return object_list


 # https://learndjango.com/tutorials/django-search-tutorial?fbclid=IwAR0K74-gcPkQ2DgMwZ9ziskykblXa5knxMnBmJvxrvAo-lN2UW_s4Q_7HAw       

