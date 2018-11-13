# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from userena.models import UserenaBaseProfile
from autoslug import AutoSlugField

# Create your models here.


class MovieGenre(TranslatableModel):
    translation = TranslatedFields(
    label = models.CharField(max_length=80),
    slug = AutoSlugField(populate_from='label')
    )

    def __unicode__(self):
        return self.label


class Movie(TranslatableModel):
    translation = TranslatedFields(
    title = models.CharField(verbose_name=_('titre'),max_length=100),
    country  = models.CharField(verbose_name=_('pays'),max_length=100),
    synopsis = models.TextField(verbose_name=_('synopsis'),),
    slug = AutoSlugField(verbose_name=_('slug'),populate_from='title'),
    )
    actors  = models.CharField(verbose_name=_('acteur'), max_length=100)
    director  = models.CharField(verbose_name=_('réalisateur'),max_length=100)
    lenght  = models.TimeField(verbose_name=_('durée'),)
    picture = models.ImageField(verbose_name=_('image'), upload_to="articles")
    release_date = models.DateField(verbose_name=_('date de sortie'),)
    rented = models.BooleanField(verbose_name=_('loué'),default=False)
    urld = models.URLField(verbose_name=_('lien vers trailer'),max_length=250)
    movie_genre = models.ManyToManyField(MovieGenre, verbose_name=_('genre'))

    def __unicode__(self):
        return self.title


class Customer(UserenaBaseProfile):
    user = models.OneToOneField(User, verbose_name=_('utilisateur'), on_delete=models.CASCADE)


class MovieRent(models.Model):
    customer = models.ForeignKey(Customer, verbose_name=_('client'))
    movie = models.ForeignKey(Movie, verbose_name=_('film'))
    checkout_date = models.DateTimeField(verbose_name=_('date de location'), auto_now_add=True)
    return_date = models.DateTimeField(verbose_name=_('date de retour'), blank=True, null=True)
    
    def __unicode__(self):
        return self.customer.user.username