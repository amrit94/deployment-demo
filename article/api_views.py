from article.serializers import (PostsSerializer, PublicationSerializer,
                                 ArticleSerializer)
from article.models import Posts, Publication, Article
from rest_framework import viewsets
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    # def perform_create(self, serializer):
    #     """Create a new object"""
    #     serializer.save(user=self.request.user)


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Creating single entry point to our API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('posts-list', request=request, format=format),
        'publication': reverse('publication-list', request=request,
                               format=format),
        'article': reverse('article-list', request=request, format=format),
        # 'users': reverse('user-list', request=request, format=format),
    })
