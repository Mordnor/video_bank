# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from parler.admin import TranslatableAdmin
from .models import Customer, Movie, MovieGenre, MovieRent

# Register your models here.

class MovieAdmin(TranslatableAdmin):
    list_display = ('id', 'title', 'director', 'actors', 'release_date', 'rented')
    list_editable = ('rented', )
    search_fields = ('rented', 'title', 'director', )


class MovieGenreAdmin(TranslatableAdmin):
    list_display = ('id', 'label')
    search_fields = ('label', )


class MovieRentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'movie', 'checkout_date')
    search_fields = ('customer', 'movie')



admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(MovieRent, MovieRentAdmin)



