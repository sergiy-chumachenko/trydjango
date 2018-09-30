from django.urls import path
from courses.views import (
    CourseView,
    CourseListView,
    CourseCreateView,
    CourseUpdateView
    # my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(),  name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')
]