from django.contrib import admin
from .models import CrochetItem, Order

admin.site.register(CrochetItem)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'item_bought', 'price', 'order_date', 'delivery_date', 'same_day')
    list_filter = ('order_date', 'delivery_date')
    search_fields = ('customer_name', 'item_bought')
    date_hierarchy = 'order_date'
