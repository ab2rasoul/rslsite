from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name = "posts")
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + "..."


@register.inclusion_tag("latestposts.html")
def latestposts():
    posts = Post.objects.filter(status=1).order_by("-published_date")[:1]
    return {'posts': posts}