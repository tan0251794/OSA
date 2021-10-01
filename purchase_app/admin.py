from django.contrib import admin

from purchase_app.models import Order, Pack, Product

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Pack)