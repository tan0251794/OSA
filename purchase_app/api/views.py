from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)

from .serializers import (
    OrderListSerializers, 
    OrderCreateSerializers,
    ProductCreateSerializers, 
    ProductListSerializers
)

from ..models import Order, Product


##------------------------------------------------------------------------------
## PRODUCT
##------------------------------------------------------------------------------

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    lookup_field= 'id'

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers

##------------------------------------------------------------------------------
## ORDER
##------------------------------------------------------------------------------

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializers

class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializers
    lookup_field= 'id'

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializers

    def perform_create(self, serializer):
        return serializer.save(customer_id=self.request.user)

class OrderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializers
    lookup_field= 'id'