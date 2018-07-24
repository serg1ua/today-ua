import json
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Article
get_articles = 10

# Create your views here.
def index(request):
    # print(dir(request))
    return HttpResponseRedirect(reverse("main"))

def main(request):

    try:
        global get_articles
        db_len = Article.objects.all().count()
        counter = db_get_len(db_len, get_articles)
        articles = Article.objects.all().order_by('-id')[:counter]
    except Article.DoesNotExist:
        raise Http404("Articles does not exist")

    context = {
        "title": "Головна",
        "articles_3": articles[:3],
        "articles_7": articles[3:10]
    }

    return render(request, "news/articles.html", context)

def section(request, selector):
    try:
        global get_articles
        db_len = Article.objects.filter(tag__iexact=selector).count()
        counter = db_get_len(db_len, get_articles)
        articles = Article.objects.filter(tag__iexact=selector).order_by('-id')[:counter]
    except Article.DoesNotExist:
        raise Http404("Articles does not exist")

    context = {
        "title": selector,
        "articles_3": articles[:3],
        "articles_7": articles[4:10]
    }
    return render(request, "news/articles.html", context)

def article(request, selector, article):
    # print(f"{selector} & {article}")
    try:
        article = Article.objects.get(header__iexact=article)
    except Article.DoesNotExist:
        raise Http404("Articles not found")
    context = {
        "article": article
    }
    return render(request, "news/article.html", context)

def api_articles(request, params):
    params = params.split('&')
    tag = params[0]
    count = int(params[1])
    try:
        if tag == 'Головна':
            db_length = db_get_len(Article.objects.all().count(), count)
            get_ten = ten_getter(db_length, count)
            articles = Article.objects.all().values()[count-10:get_ten]
        else:
            db_length = db_get_len(Article.objects.filter(tag__iexact=tag).count(), count)
            get_ten = ten_getter(db_length, count)
            articles = Article.objects.filter(tag__iexact=tag).values()[count-10:get_ten]
    except Article.DoesNotExist:
        raise Http404("Articles not found")
    return JsonResponse(list(articles), content_type='application/json', safe=False)

def api_article(request, tag, param):
    try:
        article = Article.objects.values().get(header__iexact=param)
    except Article.DoesNotExist:
        raise Http404("Articles not found")
    return JsonResponse(article, content_type='application/json', safe=False)

def db_get_len(db, artcls):
    if db < artcls:
        return artcls - (artcls - db)
    else:
        return artcls

def ten_getter(length, count):
    if (length - count) > 10:
        return 10
    else:
        return length













