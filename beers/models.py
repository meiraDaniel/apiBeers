from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Beers(models.Model):
    beer_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    rating = models.FloatField(default=0)
    url_photo = models.CharField(max_length=50, default='none')
    date_created = models.DateTimeField(default=timezone.now)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.beer_name