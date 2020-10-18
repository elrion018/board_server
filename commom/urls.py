from django.urls import path

from . import views

app_name = "commom"

urlpatterns = [
    path('article', views.article_list),
    path('article/search', views.search_article_list),
    path('article/<int:slug>', views.article_detail),
    path('article/addViews/<int:slug>', views.add_views),
    path('article/addRecommended/<int:slug>', views.add_recommended)
]
