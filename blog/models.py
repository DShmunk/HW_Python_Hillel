#from django.db import models
#
#class Post(models.Model):
#    title = models.CharField(max_length=200)
#    author = models.ForeignKey(
#        'auth.User',
#        on_delete=models.CASCADE,
#    )
#    body = models.TextField()
# 
#    def __str__(self):
#        return self.title
        
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish_at')
    created_by = models.ForeignKey(
    			User, 
    			related_name='blog_posts', 
    			on_delete=models.CASCADE,
    )
    text = models.TextField()
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

class Meta:
    ordering = ('-publish_at',)

def __str__(self):
    return self.title


class Comment(models.Model):
    post = models.ForeignKey(
    				Post, 
    				related_name='comments', 
    				on_delete=models.CASCADE,
    				)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)        
