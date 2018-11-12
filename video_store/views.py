# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from django.contrib.auth.models import User


from .models import Movie, MovieRent, Customer

# Create your views here.


# MoviesViews 
class MovieListView(ListView):
    model = Movie

class FormMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('rented', )

class MovieDetailView(DetailView):
    model = Movie
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["FormRented"] = FormMovie(initial={"movie" : self.object})
        return context

class MovieRentedView(View):
    model = Movie
    def post(self, request, *args, **kwargs):
        user = request.user
        customer = Customer.objects.get(user=user)
        slug = request.POST.get('movie_slug')
        movie = Movie.objects.get(slug=slug)
        movie.rented = True 
        movie.save()
        movieRent = MovieRent(customer=customer, movie = movie)
        movieRent.save()
        return HttpResponseRedirect(reverse('list-movie'))


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

class MovieRentListView(ListView):
    model = MovieRent
    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        user = self.kwargs['username']
        customer = Customer.objects.get(user=user)
        context['rentMovie'] = MovieRent.objects.filter(customer=user)
        return context


# UsersViews
