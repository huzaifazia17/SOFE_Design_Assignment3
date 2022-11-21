from django.contrib import admin

from .models  import  *


class ProductsAdmin(admin.ModelAdmin):
    listDisplay=('productName', 'productCode', 'productPrice')

admin.site.register(Products, ProductsAdmin)

class PurchasesAdmin(admin.ModelAdmin):
    listDisplay=('id', 'productCode', 'productName', 'productPrice', 'totalPayment')

admin.site.register(Purchases, PurchasesAdmin)