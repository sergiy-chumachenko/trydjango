from django.urls import path
from products.views import (product_create_view,
                            product_detail_view,
                            product_delete_view,
                            product_list_view,
                            product_update_view)

app_name = 'product'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
    path('<int:my_id>/', product_detail_view, name='product-detail'),
    path('<int:my_id>/update/', product_update_view, name='product-update'),
    path('create', product_create_view, name='product-create')
]
