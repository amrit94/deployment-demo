from django.urls import path
from article import api_views as views


posts_list = views.PostsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
posts_detail = views.PostsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

publication_list = views.PublicationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
publication_detail = views.PublicationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
article_list = views.ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
article_detail = views.ArticleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# user_list = views.UserViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('posts/', posts_list, name='posts-list'),
    path('posts/<int:pk>/', posts_detail, name='posts-detail'),
    path('publication/', publication_list, name='publication-list'),
    path('publication/<int:pk>/', publication_detail,
         name='publication-detail'),
    path('article/', article_list, name='article-list'),
    path('article/<int:pk>/', article_detail, name='article-detail'),
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail'),
]
