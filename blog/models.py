from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                .filter(post_status='published')


class BlogPost(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
            )
    post_title = models.CharField(max_length=250)
    post_slug = models.SlugField(max_length=250, unique_for_date="post_publish")
    post_author = models.ForeignKey(User, related_name='blog_posts')
    post_body = models.TextField()
    post_publish = models.DateTimeField(default=timezone.now)
    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)
    post_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ('-post_publish', )

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('blog:blog_post_detail', args=[self.post_slug])


