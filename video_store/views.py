# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView


from .models import Movie

# Create your views here.
class MovieListView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie


class MovieUpdateView(UpdateView):
    model = Movie
    fields = '__all__'
    template_name = 'video_store/movie_update_form.html'
    success_url="/"

class MovieCreateView(CreateView):
    model = Movie
    fields = '__all__'
    success_url="/"

class MovieDeleteView(DeleteView):
    model = Movie

    def get_success_url(self):
        return '/'