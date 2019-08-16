from django import template
from blog.models import Blog
from django.db.models import Count

register = template.Library()

@register.simple_tag(name='mytag')
def total_blog():
    blog = Blog.objects.filter(status='published')
    return blog.count()
    print("total blogs :",blog.count())

@register.inclusion_tag('blog/latest_blogs.html')
def show_latest_blogs(count=5):
    latest_blogs = Blog.objects.order_by('-publish')[:count]
    return {'latest_blogs':latest_blogs}

@register.assignment_tag
def get_most_commented_blogs(count=5):
    return Blog.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
