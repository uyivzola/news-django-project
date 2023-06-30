from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import ContactForm
from django.views.generic import TemplateView


def news_list(request):
    news_list = News.objects.all().order_by('-published_time')
    categories = Category.objects.all()
    context = {
        "news_list": news_list,
        "categories": categories
    }
    return render(request, "mohir_app/news_list.html", context=context)


def category_list(request):
    category_list = Category.objects.all()
    context = {
        'context_list': category_list
    }
    return render(request, 'mohir_app/category.html', context=context)


def news_detail(request, id):
    news = News.objects.all().order_by('-published')[:1]
    context = {
        'news': news,
        'image': news.image,
    }
    return render(request, 'mohir_app/single_page.html', context=context)


def news_detail_page(request, id):
    news = get_object_or_404(News, id=id)
    context = {
        'news': news,
    }
    return render(request, 'mohir_app/news_detail.html', context=context)


def homePageView(request):
    categories = Category.objects.all()[:20]
    news = News.objects.all()
    local_news = News.published.all().filter(category='local')[:5]
    local_one=News.published.filter(category='local').order_by('-published-time')[0]
    context = {
        'news': news,
        'categories': categories,
        'local_news': local_news,
        'local_one':local_one
    }
    return render(request, 'mohir_app/index.html', context)


def contactView(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("<h2>Tashakkur ederim!</h2>")

    context = {
        'form': form
    }
    return render(request, 'mohir_app/contact.html', context)


def page404(request):
    return render(request, 'mohir_app/404.html')


def singlePageView(request):
    single_news = News.objects.all()
    context = {
        'single_news': single_news
    }
    return render(request, 'mohir_app/single_page.html', context=context)


class ContactPageView(TemplateView):
    template_name = 'mohir_app/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'mohir_app/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h2>Biz bilan boglanganingiz uchun rahmat! </h2>')
        context = {
            'form': form
        }
        return render(request, 'mohir_app/contact.html', context)
