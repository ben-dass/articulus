from django import forms

from app.models import Article


class CreateArticleForm(forms.Form):
    ARTICLE_STATUS = (
        ("draft", "Draft"),
        ("in_progress", "In Progress"),
        ("published", "Published"),
    )

    title = forms.CharField(max_length=100)
    content = forms.TextField(widget=forms.Textarea)
    word_count = forms.IntegerField()
    twitter_post = forms.TextField(widget=forms.Textarea, required=False)
    status = forms.CharField(choices=ARTICLE_STATUS)
