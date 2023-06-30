from django.urls import path
from .views import news_list, category_list, news_detail, homePageView, contactView, page404, singlePageView

urlpatterns = [
    path('', homePageView, name='homePageView'),
    path('contact', contactView, name='contactView'),
    path('not-found', page404, name='page404'),
    path('single', singlePageView, name='singlePageView'),
    path('news', news_list, name='all_news_list'),
    path('categories', category_list, name='all_category'),
    path('<slug:slug>/', news_detail, name='news_detail')
]
