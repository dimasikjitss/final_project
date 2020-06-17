from django.contrib import admin 
from .models import Post, Category, Comment

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'category',)
    list_filter = ('created', 'publish', 'author') 
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish' 


admin.site.register(Comment)

