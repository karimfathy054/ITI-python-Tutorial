from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Cast(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name='movies')
    casts = models.ManyToManyField(Cast, related_name='movies')
    poster_image = models.ImageField(upload_to='images/',null=True,blank=True)
    
    def __str__(self):
        return self.title
       

    
class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name='series')
    casts = models.ManyToManyField(Cast, related_name='series')
    poster_image = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.title