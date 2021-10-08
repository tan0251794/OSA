from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView
)

from .serializers import (
    OrderListSerializers, 
    OrderCreateSerializers,
    OrderUpdateSerializers,
    PackListSerializers,
    ProductCreateSerializers, 
    ProductListSerializers
)

from ..models import Order, Pack, Product


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
    serializer_class = ProductCreateSerializers

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    lookup_field= 'id'

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
    serializer_class = OrderCreateSerializers

    def perform_create(self, serializer):
        return serializer.save(customer_id=self.request.user)

class OrderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializers
    lookup_field= 'id'

class OrderDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializers
    lookup_field= 'id'


##------------------------------------------------------------------------------
## PACK
##------------------------------------------------------------------------------

class PackListAPIView(ListAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackListSerializers