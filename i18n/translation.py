from .models import News

from modeltranslation.translator import TranslationOptions, register

@register(News)
class NewsTrnaslationOptions(TranslationOptions):
	fields = ['name']