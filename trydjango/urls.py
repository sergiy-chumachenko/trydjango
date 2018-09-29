from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view
from products.views import (product_create_view,
                            dynamic_lookup_view,
                            product_delete_view,
                            product_list_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('about', about_view),
    path('contacts', contact_view),
    path('products', product_list_view, name='product_list'),
    path('products/<int:my_id>/delete/', product_delete_view, name='product-delete'),
    path('products/<int:my_id>/', dynamic_lookup_view, name='product'),
    path('create', product_create_view),
    path('admin', admin.site.urls),
]
