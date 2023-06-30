from django.shortcuts import render, get_object_or_404
from .models import News, Category


def news_list(request):
    news_list = News.objects.all()
    context = {
        "news_list": news_list
    }
    return render(request, "mohir_app/news_list.html", context=context)


def category_list(request):
    category_list = Category.objects.all()
    context = {
        'context_list': category_list
    }
    return render(request, 'mohir_app/category.html', context=context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=News.Status.Published)
    image_url = news.image
    context = {
        'news': news,
        'image_url': image_url
    }
    return render(request, 'mohir_app/news_detail.html', context=context)


def homePageView(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories
    }
    return render(request, 'mohir_app/index.html', context)


def contactView(request):
    return render(request, 'mohir_app/contact.html')


def page404(request):
    return render(request, 'mohir_app/404.html')


def singlePageView(request):
    single_news = News.objects.all()
    context = {
        'single_news': single_news
    }
    return render(request, 'mohir_app/single_page.html', context=context)
