from django.shortcuts import render
from .models import Product

def home(request):
    """Главная страница"""
    return render(request, 'main/home.html')

def catalog(request):
    """Страница каталога продукции"""
    category = request.GET.get('category', '')
    search_query = request.GET.get('search', '')
    
    products = Product.objects.filter(is_active=True)
    
    if category:
        products = products.filter(category=category)
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    context = {
        'title': 'Каталог продукции',
        'products': products,
        'current_category': category,
        'search_query': search_query,
    }
    return render(request, 'main/catalog.html', context)

def about(request):
    """Страница о компании"""
    context = {
        'title': 'О компании',
        'company_info': {
            'name': 'Нефтегазтехника (НГТ)',
            'description': 'Научно-техническое предприятие, специализирующееся на производстве пакерно-якорного оборудования',
            'year_founded': '2024'
        }
    }
    return render(request, 'main/about.html', context)

def services(request):
    """Страница услуг"""
    context = {
        'title': 'Услуги',
        'services': [
            {'name': 'Производство оборудования', 'description': 'Изготовление пакерно-якорного оборудования'},
            {'name': 'Техническое обслуживание', 'description': 'Сервисное обслуживание оборудования'},
            {'name': 'Консультации', 'description': 'Технические консультации специалистов'},
        ]
    }
    return render(request, 'main/services.html', context)

def contacts(request):
    """Страница контактов"""
    context = {
        'title': 'Контакты',
        'contacts': {
            'reception_phone': '+7(3466)49-12-15',
            'sales_phone': '+7(999)549-22-25',
            'email': 'mail@ngt-nv.ru',
            'sales_email': 'fatail@ngt-nv.ru'
        }
    }
    return render(request, 'main/contacts.html', context)