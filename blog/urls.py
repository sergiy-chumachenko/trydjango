from django.urls import path
from blog.views import (ArticleListView)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(),  name='article-list'),
    # path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
    # path('<int:my_id>/', product_detail_view, name='product-detail'),
    # path('<int:my_id>/update/', product_update_view, name='product-update'),
    # path('create', product_create_view, name='product-create')
]