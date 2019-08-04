from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

from django.shortcuts import resolve_url
class Photo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username + " photo on " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        ordering = ['-updated', '-created']

    # create, update view에서 로직처리 후, redirect할 url을 위해 호출
    def get_absolute_url(self):
        return resolve_url('photo_detail', self.id)