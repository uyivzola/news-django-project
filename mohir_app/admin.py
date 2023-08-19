from django.contrib import admin
from .models import News, Category, Contact, Commentsx


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'published_time', 'status']
    list_filter = ['status', 'created_time', 'published_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'published_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']
    ordering = ['name']


@admin.register(Commentsx)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'body', 'created_time', 'active']
    list_filter = ['user', 'active']
    search_fields = ['news', 'user']
    ordering = ['news', 'created_time',]
