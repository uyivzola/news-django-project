from .models import News, Category


def latest_news(request):
    latest_news = News.objects.all().order_by('-published_time')[:10]
    context = {
        'latest_news': latest_news
    }
    return context