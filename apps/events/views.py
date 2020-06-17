from django.shortcuts import render
from .models import Event
from apps.blog.models import Category
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import EventEnrollForm

def events_list(request):
    events = Event.objects.all()
    # categories = Category.objects.all()
    return render(request, 'events/events.html', locals())

def event_detail(request, slug):
    event = Event.objects.get(slug__iexact=slug)
    # related_events = Event.objects.filter(category=event.category)
    return render(request, 'events/events_detail.html', context={'event':event})

def confirm(request):
    return render(request, 'events/confirm.html')

