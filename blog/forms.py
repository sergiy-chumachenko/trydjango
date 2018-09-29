from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Your Title'
        }))
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Your article',
            "rows": 20,
            "columns": 120,
        }
    ))

    class Meta:
        model = Article
        fields = [
            'title',
            'text'
        ]
