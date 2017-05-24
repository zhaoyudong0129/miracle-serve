from django.db import models

# Create your models here.

SEASONS = (
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Autumn', 'Autumn'),
    ('Winter', 'Winnter'),
)


class Flower(models.Model):
    title = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    seasons = models.CharField(max_length=100, blank=True, choices=SEASONS, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/flower', blank=True, null=True)
