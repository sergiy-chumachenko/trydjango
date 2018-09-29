from django.urls import path
from courses.views import (
    CourseView,
    # my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseView.as_view(template_name='contact.html'),  name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='article-detail'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')
]