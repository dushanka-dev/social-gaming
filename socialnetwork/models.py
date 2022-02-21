from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    """Users Posts section. User can create new posts"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(max_length=800, blank=True)
    slug = models.SlugField(unique=True, null=True)
    post_picture = models.ImageField(blank=True, null=True, upload_to='uploads/')
    created_time = models.DateTimeField(auto_now=True)
    post_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.author}-{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
