from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """Категории"""

    title = models.CharField(max_length=200,) 
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        verbose_name = 'category' 
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('post_category', args=[self.slug])
    def __str__(self): 
        return self.title



class Post(models.Model): 
    """Посты в категориях"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    class Meta:
        verbose_name = 'posts'
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'category': self.category.slug, 'slug':self.slug})
    
    def __str__(self): 
        return self.title

class Comment(models.Model):
    """Комментарии"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = True)
    
    def __str__(self):
        return self.comment
    
    # def get_absolute_url(self):
        # return reverse('blog_list')
     
    class Meta:
        ordering = ('author', )
