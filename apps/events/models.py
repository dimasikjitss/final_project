from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from apps.blog.models import Category

class Event(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='event_categories')
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    date = models.DateTimeField()
    mentors = models.ManyToManyField(get_user_model(), related_name='events')
    body = models.TextField(blank=True, db_index=True)
    image = models.ImageField(upload_to='event/%Y/%m/%d', blank=True)
    adress = models.CharField(max_length=50)
    company = models.CharField(max_length=100, null=True, blank=True)
    # subscription = models.ForeignKey(User,related_name='event_join',on_delete=models.CASCADE)
    class Meta:
        ordering = ('date',)

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})


    def __str__(self):
        return self.title


class JoinEvent(models.Model):
    events = models.ForeignKey(Event, related_name='events', on_delete=models.CASCADE)
