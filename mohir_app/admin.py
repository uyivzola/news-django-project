from django.contrib import admin
from .models import News, Category, Contact,Comments

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category','published_time', 'status']
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

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['news','user','body','created_time','active']
    list_filter=['news','user','active']
    search_fields=['news','user']
    ordering=['news','created_time',]