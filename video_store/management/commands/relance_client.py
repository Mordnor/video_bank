from django.core.management.base import BaseCommand
import datetime
from django.utils import timezone
from django.core.mail import EmailMessage
from video_store.models import MovieRent



class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        movie_rent = MovieRent.objects.all()
        for movie in movie_rent : 
            rented_date = movie.checkout_date
            estimate_date = rented_date + datetime.timedelta(14)
            now = timezone.now()

            if estimate_date < now : 
                print 'you got time'
            else :
                customer_email = movie.customer.user.email
                from_email = 'dorian.pitiot@gmail.com'
                to_emails = [customer_email,]
                subject = "Codi'n Camp"
                message = 'rend moi mon film'


                email = EmailMessage(subject, message, from_email, to_emails)
                email.encoding = 'us-ascii'
                print email




