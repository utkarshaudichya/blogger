from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Blog(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog')
    body = models.TextField('Blog')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[self.id, self.publish.year, self.publish.strftime('%m'),
                                    self.publish.strftime('%d'), self.slug])

class Comments(models.Model):
    blog = models.ForeignKey(Blog)
    user = models.ForeignKey(User)
    body = models.TextField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('Comments', related_name='replies', null=True) #also use 'self' in place of 'Comments'
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return '{}--{}'.format(self.blog.title, str(self.user.username))
