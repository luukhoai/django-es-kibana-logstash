from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .utils import BlogPostIndex
import logging

logger = logging.getLogger('django_web')



class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def indexing(self):
        obj = BlogPostIndex(
            meta={'id': self.id},
            author=self.author.username,
            title=self.title,
            text=self.text,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    def save(self, *args, **kwargs):
        if not self.id or not self.created_at:
            self.created_at = timezone.localtime()
        self.updated_at = timezone.localtime()
        blogpost = super(BlogPost, self).save(*args, **kwargs)
        self.indexing()
        return blogpost