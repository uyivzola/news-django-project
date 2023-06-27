from django.contrib import admin
from .models import News, Category


# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display=['title','slug','publish_time','status']

# admin.site.register(News)
# admin.site.register(Category)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_time', 'status']
    list_filter = ['status', 'created_time', 'published_time',]
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'published_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
