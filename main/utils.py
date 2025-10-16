from django.utils.translation import get_language

def get_localized_product_data(product):
    """Возвращает локализованные данные продукта"""
    lang = get_language()
    
    # Для простоты, если не используем i18n, можно передавать язык через request
    # или использовать отдельную логику
    
    return {
        'id': product.id,
        'name': getattr(product, f'name_{lang}', product.name_ru),
        'short_description': getattr(product, f'short_description_{lang}', product.short_description_ru),
        'description': getattr(product, f'description_{lang}', product.description_ru),
        'features': getattr(product, f'features_{lang}', product.features_ru),
        'application': getattr(product, f'application_{lang}', product.application_ru),
        'image': product.image,
        'category': product.category,
    }