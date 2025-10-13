from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'category', 'short_description', 'description', 'features', 'application', 'is_active')
        }),
            ('Изображение', {
            'fields': ('image',)
        }),
    )
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets

admin.site.register(Product, ProductAdmin)