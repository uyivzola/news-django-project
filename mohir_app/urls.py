from django.urls import path
from .views import news_list, category_list,news_detail

urlpatterns = [
    path('news', news_list, name='all_news_list'),
    path('categories', category_list, name='all_category'),
    path('<slug:slug>/', news_detail, name='news_detail')
    ]
