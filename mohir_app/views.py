from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import ContactForm
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from news_project.custom_permissions import OnlyLoggedSuperUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CommentForm


def news_detail_page(request, slug):
    # Get the News object with the given slug, and make sure it has the status 'Published'
    news = get_object_or_404(News, slug=slug, status=News.Status.Published)

    # Get all active comments associated with the news
    comments = news.comments.filter(active=True)

    # Create a new_comment variable to store the new comment (if any) - initialize it to None
    new_comment = None

    # Check if the request method is POST (i.e., a form submission)
    if request.method == 'POST':
        # Create a CommentForm instance and bind it to the request data
        comment_form = CommentForm(data=request.POST)

        # Check if the form data is valid
        if comment_form.is_valid():
            # Create a new comment object but don't save it to the database yet
            new_comment = comment_form.save(commit=False)
            # Associate the comment with the corresponding news object
            new_comment.news = news
            # Associate the comment with the corresponding user object
            new_comment.user = request.user
            # Save it to the database
            new_comment.save()
            # after submitting clear input text to write another comment
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    # Prepare the context dictionary with the all objects
    context = {
        'news': news,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    # Render the 'news_detail.html' template with the context
    return render(request, 'mohir_app/news_detail.html', context=context)


class HomePageView(ListView):
    model = News
    template_name = "mohir_app/index.html"
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by('-id')[:20]
        context['latest_post'] = News.objects.all().order_by(
            '-published_time')[:4]
        context['local_news'] = News.objects.all().order_by(
            '-published_time')[:6]
        context['prezident'] = News.objects.all().filter(
            category__name='Prezident').order_by('-published_time')
        context['business'] = News.objects.all().filter(
            category__name='Business').order_by('-published_time')
        context['arts'] = News.objects.all().filter(
            category__name='Arts').order_by('-published_time')
        context['technology'] = News.objects.all().filter(
            category__name='Technology').order_by('-published_time')
        context['ethnic'] = News.objects.all().filter(
            category__name='Ethnic').order_by('-published_time')
        return context


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
            return render(request, 'mohir_app/form_success.html')
        context = {
            'form': form
        }
        return render(request, 'mohir_app/contact.html', context)


class BusinessNewsView(TemplateView):
    model = News
    template_name = 'mohir_app/business.html'
    context_object_name = 'business_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Business')
        return news


class TechnologyNewsView(TemplateView):
    model = News
    template_name = 'mohir_app/technology.html'
    context_object_name = 'technology_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Technology')
        return news


class ArtsNewsView(TemplateView):
    model = News
    template_name = 'mohir_app/arts.html'
    context_object_name = 'arts_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Arts')
        return news


class NewsUpdateView(OnlyLoggedSuperUser, UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'


class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('homePageView')


class NewsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_page_view(request):
    admin_users = User.objects.filter(is_superuser=True)
    context = {
        'admin_users': admin_users
    }
    return render(request, 'pages/admin_page.html', context)

class SearchResults(ListView):
    model = News
    template_name = 'mohir_app/search_result.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return News.objects.filter(title__icontains=query)
        return News.objects.none()  # Return an empty queryset if no query
