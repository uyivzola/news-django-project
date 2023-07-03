from django.urls import path
from .views import news_list, category_list, news_detail, homePageView, ContactPageView, page404, singlePageView, news_detail_page, HomePageView, BusinessNewsView, TechnologyNewsView, ArtsNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='homePageView'),
    path('contact', ContactPageView.as_view(), name='contactView'),
    path('not-found', page404, name='page404'),
    path('business/', BusinessNewsView.as_view(), name='businessNewsView'),
    path('news', news_list, name='all_news_list'),
    path('categories', category_list, name='all_category'),
    path('single/', news_detail, name='singlePageView'),
    path('arts/', ArtsNewsView.as_view(), name='artsNewsView'),
    path('<slug:slug>/', news_detail_page, name='news_detail_page'),
    path('technology/', TechnologyNewsView.as_view(), name='technologyNewsView'),

]
