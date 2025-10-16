from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Русская версия (основная)
    path('', views.home_ru, name='home_ru'),
    path('catalog/', views.catalog_ru, name='catalog_ru'),
    path('about/', views.about_ru, name='about_ru'),
    path('services/', views.services_ru, name='services_ru'),
    path('contacts/', views.contacts_ru, name='contacts_ru'),
    
    # Английская версия
    path('en/', views.home_en, name='home_en'),
    path('en/catalog/', views.catalog_en, name='catalog_en'),
    path('en/about/', views.about_en, name='about_en'),
    path('en/services/', views.services_en, name='services_en'),
    path('en/contacts/', views.contacts_en, name='contacts_en'),
    
    # Азербайджанская версия
    path('az/', views.home_az, name='home_az'),
    path('az/catalog/', views.catalog_az, name='catalog_az'),
    path('az/about/', views.about_az, name='about_az'),
    path('az/services/', views.services_az, name='services_az'),
    path('az/contacts/', views.contacts_az, name='contacts_az'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)