from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from miracle_server import settings

SEASONS = (
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Autumn', 'Autumn'),
    ('Winter', 'Winnter'),
)


class Flower(models.Model):
    """
     the feature of the flower
    """
    title = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    seasons = models.CharField(max_length=100, blank=True, choices=SEASONS, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/flower', blank=True, null=True)
    smell = models.CharField(max_length=100, blank=True, null=True)
    scenarios = models.CharField(max_length=100, blank=True, null=True)
    slogan = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Scene(models.Model):
    """
    the feature of the scene, it can conclude weather, usage, scenario,mode, constellation,style,...
    """
    title = models.CharField(max_length=200, unique=True)
    detail = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/scene', blank=True, null=True)

    def __str__(self):
        return self.title


class Design(models.Model):
    """
    the feature of the design
    """
    title = models.CharField(max_length=200, unique=True)
    detail = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/scene', blank=True, null=True)
    scenes = models.ManyToManyField(Scene, blank=True, related_name='designs')
    flowers = models.ManyToManyField(Flower, blank=True)

    def __str__(self):
        return self.title


class UserClick(models.Model):
    scene = models.ForeignKey(Scene)
    design = models.ForeignKey(Design)
    click_time = models.DateTimeField(default=timezone.now)


class Order(models.Model):
    scene = models.ForeignKey(Scene, related_name='orders')
    design = models.ForeignKey(Design, blank=True, null=True, related_name='orders')

    # 备注
    remark = models.CharField(max_length=500, blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, default=timezone.now)
    # 付款\配送\送达\取消
    status = models.CharField(max_length=20, blank=True, default=True)

    contact = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
