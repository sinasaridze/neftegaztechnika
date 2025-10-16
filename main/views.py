from django.shortcuts import render
from .models import Product

# Русская версия
def home_ru(request):
    return render(request, 'main/ru/home.html')

def catalog_ru(request):
    products = Product.objects.filter(is_active=True)
    
    # Добавляем локализованные данные к каждому продукту
    for product in products:
        product.localized_name = product.get_localized_name('ru')
        product.localized_short_description = product.get_localized_short_description('ru')
        product.localized_description = product.get_localized_description('ru')
        product.localized_features = product.get_localized_features('ru')
        product.localized_application = product.get_localized_application('ru')
    
    return render(request, 'main/ru/catalog.html', {'products': products})

def about_ru(request):
    return render(request, 'main/ru/about.html')

def services_ru(request):
    return render(request, 'main/ru/services.html')

def contacts_ru(request):
    return render(request, 'main/ru/contacts.html')

# Английская версия
def home_en(request):
    return render(request, 'main/en/home.html')

def catalog_en(request):
    products = Product.objects.filter(is_active=True)
    
    # Добавляем локализованные данные к каждому продукту
    for product in products:
        product.localized_name = product.get_localized_name('en')
        product.localized_short_description = product.get_localized_short_description('en')
        product.localized_description = product.get_localized_description('en')
        product.localized_features = product.get_localized_features('en')
        product.localized_application = product.get_localized_application('en')
    
    return render(request, 'main/en/catalog.html', {'products': products})

def about_en(request):
    return render(request, 'main/en/about.html')

def services_en(request):
    return render(request, 'main/en/services.html')

def contacts_en(request):
    return render(request, 'main/en/contacts.html')

# Азербайджанская версия
def home_az(request):
    return render(request, 'main/az/home.html')

def catalog_az(request):
    products = Product.objects.filter(is_active=True)
    
    # Добавляем локализованные данные к каждому продукту
    for product in products:
        product.localized_name = product.get_localized_name('az')
        product.localized_short_description = product.get_localized_short_description('az')
        product.localized_description = product.get_localized_description('az')
        product.localized_features = product.get_localized_features('az')
        product.localized_application = product.get_localized_application('az')
    
    return render(request, 'main/az/catalog.html', {'products': products})

def about_az(request):
    return render(request, 'main/az/about.html')

def services_az(request):
    return render(request, 'main/az/services.html')

def contacts_az(request):
    return render(request, 'main/az/contacts.html')