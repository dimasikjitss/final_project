from django.contrib import admin
from .models import Event, JoinEvent


@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(JoinEvent)
