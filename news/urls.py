from django.urls import path

from .views import index, main, section, article, api_articles, api_article
urlpatterns = [
    path("", index, name="index"),
    path("main", main, name="main"),
    path("news/<str:selector>", section, name="section"),
    path("news/<str:selector>/<str:article>", article, name="article"),
    path("api/articles/<str:params>", api_articles),
    path("news/<str:tag>/api/article/<str:param>", api_article)
]