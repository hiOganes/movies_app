from django.db import models
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class MoviesModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    poster = models.ImageField(
        upload_to='poster/%Y/%m/%d/', 
        blank=True, 
        default='poster/Out_Of_Poster.jpg'
        )
    slug = models.SlugField(max_length=255, unique=True)
    rating = models.ManyToManyField(User)


    objects = models.Manager()
    tags = TaggableManager()


    class Meta:
        ordering = ['-release_date']
        # indexes = [models.Index(fields=['title'])]


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie', args=[self.slug])
