from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
    DeleteView
)
from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() #articles/<model>name_list.html


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)