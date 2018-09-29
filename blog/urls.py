from django.urls import path
from blog.views import (ArticleListView,
                        ArticleDetailView)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(),  name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('<int:my_id>/delete/', product_delete_view, name='product-delete'),

    # path('<int:my_id>/update/', product_update_view, name='product-update'),
    # path('create', product_create_view, name='product-create')
]