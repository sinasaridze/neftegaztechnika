from modeltranslation.translator import translator, TranslationOptions
from .models import Product

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'short_description', 'features', 'application')

translator.register(Product, ProductTranslationOptions)
