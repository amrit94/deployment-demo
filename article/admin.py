from django.contrib import admin
from article.models import Posts, Article, Publication

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','is_active', 'date_posted']
    list_editable = ['is_active']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline','is_active']
    list_editable = ['is_active']
admin.site.register(Article, ArticleAdmin)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']
