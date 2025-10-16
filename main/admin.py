from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = (
        'name_ru', 'name_en', 'name_az',
        'short_description_ru', 'short_description_en', 'short_description_az'
    )

    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'is_active', 'image')
        }),
        ('Название', {
            'fields': ('name_ru', 'name_en', 'name_az')
        }),
        ('Краткое описание', {
            'fields': ('short_description_ru', 'short_description_en', 'short_description_az')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_az')
        }),
        ('Особенности', {
            'fields': ('features_ru', 'features_en', 'features_az')
        }),
        ('Область применения', {
            'fields': ('application_ru', 'application_en', 'application_az')
        }),
    )
