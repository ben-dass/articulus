from django.shortcuts import render
from app.forms import CreateArticleForm
from app.models import Article


def home(request):
    articles = Article.objects.all()
    return render(
        request,
        "app/home.html",
        {
            "articles": articles,
        },
    )


def create_article(request):
    if request.method == "POST":
        pass
    else:
        form = CreateArticleForm()
    return render(request, "app/create_article.html", {"form": form})
