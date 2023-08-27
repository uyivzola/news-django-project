from modeltranslation.translator import TranslationOptions, register
from .models import News, Category, Commentsx

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')  # Add fields to translate

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # Add fields to translate

@register(Commentsx)
class CommentsxTranslationOptions(TranslationOptions):
    fields = ('body',)  # Add fields to translate
