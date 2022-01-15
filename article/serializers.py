from rest_framework import serializers
from article.models import Posts, Publication, Article
from django.contrib.auth.models import User


class PostsSerializer(serializers.ModelSerializer):
    # author = serializers.HyperlinkedRelatedField(view_name='user-detail',
    #                                              read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Posts
        fields = ['id', 'url', 'title', 'content', 'author', 'is_active']


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'url', 'title', 'is_active']


class ArticleSerializer(serializers.ModelSerializer):
    # publications = serializers.StringRelatedField()
    publications = serializers.PrimaryKeyRelatedField(many=True,
                    queryset=Publication.objects.all())

    class Meta:
        model = Article
        fields = ['id', 'url', 'headline', 'publications', 'is_active']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']
