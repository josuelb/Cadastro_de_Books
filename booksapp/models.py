from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pags = models.IntegerField()
    publishing = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
