from django.urls import path

from purchase_app.api.views import (
    OrderCreateAPIView,
    OrderUpdateAPIView,
    ProductCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    OrderListAPIView,
    OrderDetailAPIView,
)

urlpatterns = [
    #PRODUCT
    path('product/', ProductListAPIView.as_view(), name='list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='create'),
    path('product/<slug:id>/', ProductDetailAPIView.as_view(), name='detail'),
    # path('<slug:slug>/edit/', PostListAPIView.as_view(), name='update'),
    # path('<slug:slug>/delete/', PostListAPIView.as_view(), name='delete'),

    #ORDER
    path('order/', OrderListAPIView.as_view(), name='list'),
    path('order/create/', OrderCreateAPIView.as_view(), name='create'),
    path('order/<slug:id>/', OrderDetailAPIView.as_view(), name='detail'),
    path('order/<slug:slug>/edit/', OrderUpdateAPIView.as_view(), name='update'),
    # path('<slug:slug>/delete/', PostListAPIView.as_view(), name='delete'),
]