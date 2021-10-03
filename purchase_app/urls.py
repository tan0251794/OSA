from django.urls import path

from purchase_app.views import (
    delete_product,
    increase_product,
    order, 
    order_edit, 
    pack,
    pack_edit, 
    product,
    update_product
    )

urlpatterns = [
    #ORDER VIEWS
    path('', order, name='cms-order'),
    path('order/edit/', order_edit, name='cms-order-edit'),
    #PRODUCT VIEWS
    path('order/edit/product/<int:product_id>', update_product, name='update-product'),
    path('order/edit/create/<int:_id>', increase_product, name='increase-product'),
    path('order/edit/delete/<int:_id>/<int:product_id>', delete_product, name='delete-product'),
    path('product/', product, name='cms-product'),
    #PACK VIEWS
    path('pack/', pack, name='cms-pack'),
    path('pack/edit/', pack_edit, name='cms-pack-edit'),
]