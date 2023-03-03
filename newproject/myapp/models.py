from django.db import models

# Create your models here.

class Place(models.Model):
    objects = None
    Name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pics')
    Description = models.TextField()

class Team(models.Model):
    objects = None
    Name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='team')
    Description = models.TextField()




