from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('packers', 'Пакеры'),
        ('anchors', 'Якоря'),
        ('assemblies', 'Компоновки'),
        ('parts', 'Запчасти'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Название товара')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    short_description = models.TextField(max_length=500, verbose_name='Краткое описание')
    features = models.TextField(verbose_name='Отличительные особенности и преимущества', blank=True)
    application = models.TextField(verbose_name='Область применения', blank=True)
    
    
    # Изображение
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')
    
    # Дополнительные поля
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
    
    def __str__(self):
        return self.name