from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
#models
from .models import Article

#serializers
from .serializers import ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article_list = Article.objects.all()
        articleSerializer = ArticleSerializer(article_list, many=True)
        return Response(articleSerializer.data)

    elif request.method == 'POST':
        articleSerializer = ArticleSerializer(data=request.data)
        if articleSerializer.is_valid():
            article = articleSerializer.save()
            article.views = 0
            article.recommended = 0
            article.save()
            return_serializer = ArticleSerializer(article)
            return Response(return_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(return_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request, slug):

    try:
        article = Article.objects.get(slug=slug)
    except article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        articleSerializer = ArticleSerializer(article)
        return Response(articleSerializer.data)

    elif request.method == 'PUT':
        articleSerializer = ArticleSerializer(article, data=request.data)
        if articleSerializer.is_valid():
            articleSerializer.save()
            return Response(articleSerializer.data)
        return Response(articleSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)