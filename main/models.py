from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('packers', 'Пакеры'),
        ('anchors', 'Якоря'),
        ('packer assemblies', 'Пакерные компоновки'),
        ('valves and well chambers', 'Клапаны и скважинные камеры'),
        ('disconnectors and others', 'Разъединители и другое'),
    ]

    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        verbose_name='Категория'
    )

    # --- Названия ---
    name_ru = models.CharField(max_length=200, verbose_name='Название (рус.)')
    name_en = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название (англ.)')
    name_az = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название (азерб.)')

    # --- Краткое описание ---
    short_description_ru = models.TextField(max_length=500, verbose_name='Краткое описание (рус.)')
    short_description_en = models.TextField(max_length=500, blank=True, null=True, verbose_name='Краткое описание (англ.)')
    short_description_az = models.TextField(max_length=500, blank=True, null=True, verbose_name='Краткое описание (азерб.)')

    # --- Полное описание ---
    description_ru = models.TextField(verbose_name='Описание (рус.)')
    description_en = models.TextField(blank=True, null=True, verbose_name='Описание (англ.)')
    description_az = models.TextField(blank=True, null=True, verbose_name='Описание (азерб.)')

    # --- Особенности ---
    features_ru = models.TextField(blank=True, null=True, verbose_name='Особенности (рус.)')
    features_en = models.TextField(blank=True, null=True, verbose_name='Особенности (англ.)')
    features_az = models.TextField(blank=True, null=True, verbose_name='Особенности (азерб.)')

    # --- Область применения ---
    application_ru = models.TextField(blank=True, null=True, verbose_name='Область применения (рус.)')
    application_en = models.TextField(blank=True, null=True, verbose_name='Область применения (англ.)')
    application_az = models.TextField(blank=True, null=True, verbose_name='Область применения (азерб.)')

    # Изображение
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )

    # Активен / неактивен
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name_ru']

    def __str__(self):
        return self.name_ru

    # Методы для получения локализованных данных
    def get_localized_name(self, lang='ru'):
        """Возвращает локализованное название"""
        field_name = f'name_{lang}'
        localized_name = getattr(self, field_name, None)
        # Если локализованное название пустое, используем русскую версию как fallback
        if not localized_name:
            return self.name_ru
        return localized_name

    def get_localized_short_description(self, lang='ru'):
        """Возвращает локализованное краткое описание"""
        field_name = f'short_description_{lang}'
        localized_desc = getattr(self, field_name, None)
        if not localized_desc:
            return self.short_description_ru
        return localized_desc

    def get_localized_description(self, lang='ru'):
        """Возвращает локализованное описание"""
        field_name = f'description_{lang}'
        localized_desc = getattr(self, field_name, None)
        if not localized_desc:
            return self.description_ru
        return localized_desc

    def get_localized_features(self, lang='ru'):
        """Возвращает локализованные особенности"""
        field_name = f'features_{lang}'
        localized_features = getattr(self, field_name, None)
        if not localized_features:
            return self.features_ru or ""
        return localized_features

    def get_localized_application(self, lang='ru'):
        """Возвращает локализованную область применения"""
        field_name = f'application_{lang}'
        localized_application = getattr(self, field_name, None)
        if not localized_application:
            return self.application_ru or ""
        return localized_application

    # Свойства для удобства (опционально)
    @property
    def name(self):
        """Возвращает название на текущем языке (по умолчанию русский)"""
        return self.get_localized_name('ru')

    @property
    def short_description(self):
        return self.get_localized_short_description('ru')

    @property
    def description(self):
        return self.get_localized_description('ru')

    @property
    def features(self):
        return self.get_localized_features('ru')

    @property
    def application(self):
        return self.get_localized_application('ru')