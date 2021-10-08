from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import Product, Order, Pack


##------------------------------------------------------------------------------
## PRODUCT
##------------------------------------------------------------------------------
class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = [
            'id',
            'product_name',
            'quantity',
            'product_url',
            'order',
            'pack',
            'price',
            'total_price',
            'estimated_weight',
            'measurement_weight',
            'status',
            'ship_company',
            'comfirm_notifed_fig',
            'memo_from_customer',
        ]

class ProductCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = [
            'product_url',
            'product_name',
            'quantity',
            'memo_from_customer',
            'order'
        ]


##------------------------------------------------------------------------------
## ORDER
##------------------------------------------------------------------------------
class OrderListSerializers(serializers.ModelSerializer):

    products = SerializerMethodField()

    class Meta:
        model = Order 
        fields = [
            'id',
            'order_no',
            'order_date',
            'customer_id',
            'customer_name',
            'customer_phone',
            'customer_address',
            'customer_email',
            'products',
            'status',
            'total_product_price',
            'estimated_total_weight',
            'estimated_ship_fee',
            'estimated_total_fee',
            'fix_total_weight',
            'fix_ship_fee',
            'fix_total_fee',
            'domestic_delivery_method',
            'payment_method',
            'memo',
            'delivery_date',
            'delivery_time',
    ]

    def get_products(self, obj):
        products = Product.objects.filter(order_id=obj.id)
        return ProductListSerializers(products, many=True).data

class OrderCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = [
            # 'order_no',
            'order_date',
            'customer_name',
            'customer_phone',
            'customer_address',
            'customer_email',
            'domestic_delivery_method',
            'payment_method',
    ]

class OrderUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = [
            # 'order_no',
            'order_date',
            # 'customer_id',
            'customer_name',
            'customer_phone',
            'customer_address',
            'customer_email',
            'status',
            # 'total_product_price',
            # 'estimated_total_weight',
            # 'estimated_ship_fee',
            # 'estimated_total_fee',
            'fix_total_weight',
            'fix_ship_fee',
            'fix_total_fee',
            'domestic_delivery_method',
            'payment_method',
            'memo',
            'delivery_date',
            'delivery_time',
    ]


    
##------------------------------------------------------------------------------
## PACK
##------------------------------------------------------------------------------
class PackListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Pack 
        fields = '__all__'