from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField


class review(models.Model):
    name = models.CharField(max_length=30, blank=False)
    mail = models.EmailField(max_length=30)
    contact = models.IntegerField()
    text = models.TextField()
# Create your models here.
