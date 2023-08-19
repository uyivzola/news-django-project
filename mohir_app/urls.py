from django.urls import path
from .views import ContactPageView, page404, news_detail_page,HomePageView, NewsUpdateView, NewsDeleteView, NewsCreateView, admin_page_view, SearchResults
urlpatterns = [
    path('', HomePageView.as_view(), name='homePageView'),
    path('contact', ContactPageView.as_view(), name='contactView'),
    path('not-found', page404, name='page404'),
    path('<slug:slug>/', news_detail_page, name='news_detail_page'),
    path('<slug>/edit', NewsUpdateView.as_view(), name='newsUpdateView'),
    path('<slug>/delete', NewsDeleteView.as_view(), name='newsDeleteview'),
    path('create/', NewsCreateView.as_view(), name='newsCreate'),
    path('admin-page/', admin_page_view, name='admin_page'),
    path('searchresult/', SearchResults.as_view(), name='search_results'),
]
