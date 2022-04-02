from django.contrib import admin

from apps.products.models import Product, Purchase


admin.site.register(Product)
admin.site.register(Purchase)

