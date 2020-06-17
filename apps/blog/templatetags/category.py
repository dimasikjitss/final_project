from django import template
from apps.blog.models import Category, Post

register = template.Library()

@register.inclusion_tag('blog/post/category.html')
def list_category():
    return {'categories' : Category.objects.all()}


@register.inclusion_tag('blog/post/posts.html')
def list_post():
    # return {'posts' : Post.objects.all()[0:3]}
    return {'posts': Post.objects.filter()[0:5]}
