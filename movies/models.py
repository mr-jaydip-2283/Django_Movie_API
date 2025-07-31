from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name