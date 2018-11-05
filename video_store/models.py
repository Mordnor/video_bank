# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile
from autoslug import AutoSlugField

# Create your models here.


class MovieGenre(models.Model):
    label = models.CharField(max_length=80)
    slug = AutoSlugField(populate_from='label')

    def __unicode__(self):
        return self.label


class Movie(models.Model):
    actors  = models.CharField(max_length=100)
    country  = models.CharField(max_length=100)
    director  = models.CharField(max_length=100)
    lenght  = models.TimeField()
    picture = models.ImageField(upload_to="articles")
    release_date = models.DateField()
    rented = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title')
    synopsis = models.TextField()
    title = models.CharField(max_length=100)
    urld = models.URLField(max_length=250)
    movie_genre = models.ManyToManyField(MovieGenre)

    def __unicode__(self):
        return self.title


class Customer(UserenaBaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class MovieRent(models.Model):
    customer = models.ForeignKey(Customer)
    movie = models.ForeignKey(Movie)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.customer.user.username