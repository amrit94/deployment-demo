from django.shortcuts import render
from article.models import Posts


def home(request):
    posts = Posts.objects.all()
    content = {'posts': posts}
    
    return render(request, 'article/home.html', content)
