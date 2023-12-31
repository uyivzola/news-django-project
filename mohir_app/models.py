from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=News.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    @classmethod
    def published(cls):
        return cls.objects.filter(status=cls.Status.Published)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='mohir_app/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices,
                              default=Status.Draft)
    viewed_ips = models.TextField(default='')
    views_count = models.IntegerField(default=0)

    objects = models.Manager()
    published = PublishedManager()

    # @classmethod
    # def published(cls):
    #     return cls.objects.filter(status=News.Status.Published)

    class Meta:
        ordering = ['-published_time']

    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])

    def __str__(self):
        return self.title
    # giving SEO slug for pages


class Commentsx(models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='comments'
                             )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return self.body


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.email
