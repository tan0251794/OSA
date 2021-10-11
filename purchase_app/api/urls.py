from django.urls import path

from purchase_app.api.views import (
    OrderCreateAPIView,
    OrderDeleteAPIView,
    OrderUpdateAPIView,
    PackListAPIView,
    ProductCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    OrderListAPIView,
    OrderDetailAPIView,
    ProductUpdateAPIView,
)

urlpatterns = [
    #PRODUCT
    path('product/', ProductListAPIView.as_view(), name='list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='create'),
    path('product/<slug:id>/', ProductDetailAPIView.as_view(), name='detail'),
    path('product/<slug:id>/edit/', ProductUpdateAPIView.as_view(), name='update'),
    #path('<slug:slug>/delete/', PostListAPIView.as_view(), name='delete'),

    #ORDER
    path('order/', OrderListAPIView.as_view(), name='order-list'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('order/<slug:id>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('order/<slug:id>/edit/', OrderUpdateAPIView.as_view(), name='order-update'),
    path('order/<slug:id>/delete/', OrderDeleteAPIView.as_view(), name='order-delete'),

    #PACK
    path('pack/', PackListAPIView.as_view(), name='list'),
]