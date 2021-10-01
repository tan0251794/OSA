from django.urls import path

from purchase_app.views import (
    order, 
    order_edit, 
    pack, 
    product
    )

urlpatterns = [
    path('', order, name='cms-order'),
    path('order/edit/', order_edit, name='cms-order-edit'),
    path('product/', product, name='cms-product'),
    path('pack/', pack, name='cms-pack'),
]