from django import forms
from sampleapp.models import NewsArticle


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'date', 'intro', 'body', 'main_image', 'og_image', 'tags']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'body': forms.Textarea(attrs={'rows': 10}),
        }
