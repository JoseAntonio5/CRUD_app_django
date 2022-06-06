from django.db import models
from django.contrib.auth.models import User

# model User is default from django.contrib.auth.models
# TODO: make a User model have the field 'posts'

class PostModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    posted_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title