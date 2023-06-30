from django.urls import path
from .views import news_list, category_list, news_detail, homePageView, ContactPageView, page404, singlePageView,news_detail_page

urlpatterns = [
    path('', homePageView, name='homePageView'),
    path('contact', ContactPageView.as_view(), name='contactView'),
    path('not-found', page404, name='page404'),
    # path('single', singlePageView, name='singlePageView'),
    path('news', news_list, name='all_news_list'),
    path('categories', category_list, name='all_category'),
    path('single/', news_detail, name='singlePageView'),
    path('<int:id>/', news_detail_page, name='news_detail_page')
]
