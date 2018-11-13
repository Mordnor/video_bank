"""video_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from userena.views import signup, profile_edit, profile_detail, password_change
from userena.views import email_change, email_confirm, direct_to_user_template



from video_store.views import MovieListView, MovieDetailView, MovieUpdateView
from video_store.views import MovieCreateView, MovieDeleteView, MovieRentedView, MovieRentListView



urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^movie/(?P<slug>[-\w]+)/rented/$', MovieRentedView.as_view(), name='rented-movie'),

    url(r'^login/$', auth_views.LoginView.as_view()),

    url(r'^$', MovieListView.as_view(), name='list-movie'),
    url(r'^movie/create/$', MovieCreateView.as_view(), name='create-movie'),
    url(r'^movie/(?P<slug>[-\w]+)/$', MovieDetailView.as_view(), name='detail-movie'),
    url(r'^movie/(?P<slug>[-\w]+)/update/$', MovieUpdateView.as_view(), name='update-movie'),
)


urlpatterns += [


    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),



    url(r'^located/(?P<username>[-\w]+)/$', MovieRentListView.as_view(), name='list-rent-movie'),
    url(r'^movie/(?P<slug>[-\w]+)/delete/$', MovieDeleteView.as_view(), name='delete-movie'),


    # Userena
    url(r'^user/create/$', signup ,{'success_url':'/'}, name="create-user"),
    url(r'^(?P<username>(?!(signout|signup|signin)/)[\@\.\+\w-]+)/$', profile_detail,name='userena_profile_detail'),

    url(r'^(?P<username>[\@\.\+\w-]+)/edit/$', profile_edit ,name='userena_profile_edit'),

   # Change email and confirm it
    url(r'^(?P<username>[\@\.\+\w-]+)/email/$', email_change, name='userena_email_change'),
    url(r'^(?P<username>[\@\.\+\w-]+)/email/complete/$', direct_to_user_template, {'template_name': 'userena/email_change_complete.html'}, name='userena_email_change_complete'),
    url(r'^(?P<username>[\@\.\+\w-]+)/confirm-email/complete/$', direct_to_user_template,{'template_name': 'userena/email_confirm_complete.html'},name='userena_email_confirm_complete'),
    url(r'^confirm-email/(?P<confirmation_key>\w+)/$', email_confirm, name='userena_email_confirm'),

    # Change password
    url(r'^(?P<username>[\@\.\+\w-]+)/password/$', password_change, name='userena_password_change'),
    url(r'^(?P<username>[\@\.\+\w-]+)/password/complete/$',direct_to_user_template,{'template_name': 'userena/password_complete.html'}, name='userena_password_change_complete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
