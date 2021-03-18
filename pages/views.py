from django.shortcuts import render
from article.models import Article


def main_page(request):
    articles = Article.objects.all()
    article = articles.first()
    context = {
        'articles': articles,
        'article': article
    }
    return render(request, 'pages/main_page.html', context=context)
