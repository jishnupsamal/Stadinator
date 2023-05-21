from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_code', 'name', 'price', 'in_stock']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'Product', 'User', 'seat', 'phone', 'ordered_at']
    fields = ('Product', 'User', 'seat', 'phone', 'ordered_at', 'delivered')
    readonly_fields = ['Product', 'User', 'seat', 'phone', 'ordered_at']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)