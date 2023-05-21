from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    ProductUpdate,
    ProductCreate,
    ProductDelete,
    OrderCreate,
    Orders,
    OrdersUpdate,
    MyOrders,
)

app_name = 'store'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('new/', ProductCreate.as_view(), name='create'),
    # path('orders/', Orders.as_view(), name='list_orders'),
    path('orders/', Orders.as_view(), name='list_orders'),
    path('orders/<int:pk>/update', OrdersUpdate.as_view(), name='update_orders'),
    path('<slug:slug>/', ProductDetail.as_view(), name='detail'),
    path('<slug:slug>/order/', OrderCreate.as_view(), name='order'),
    path('<slug:slug>/update/', ProductUpdate.as_view(), name='update'),
    path('<slug:slug>/delete/', ProductDelete.as_view(), name='delete'),
]
