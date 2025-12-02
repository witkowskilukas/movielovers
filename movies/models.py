from django.db import models

# Create your models here.

class Movie(models.Model):
        title = models.CharField(max_length=35)
        genre  = models.CharField(max_length=20)
        director = models.CharField(max_length=35)
        year = models.IntegerField(default=1990)

        def __str__(self):
            return self.title
