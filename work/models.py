from django.db import models
from taggit.managers import TaggableManager


class Work(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=title)
    excerpt = models.TextField(null=True, blank=True)
    link = models.URLField()
    date = models.DateTimeField()
    tags = TaggableManager()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title
