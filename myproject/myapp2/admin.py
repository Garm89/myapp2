from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name', 'email', 'registration_date']
    search_fields = ['email']
    search_help_text = 'Поиск по полю Почта (email)'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount']
    list_filter = ['client', 'order_date']
    search_fields = ['products']
    search_help_text = 'Поиск по полю Товар (products)'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']
    list_filter = ['added_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'



admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
