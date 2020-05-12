from django.urls import path

from . import views

app_name = "commom"

urlpatterns = [
  path('article', views.article_list),
  path('article/<int:slug>', views.article_detail)
]